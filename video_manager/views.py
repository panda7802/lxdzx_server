# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import urllib
import urllib2

from django.http import HttpResponse, HttpRequest, StreamingHttpResponse
from django.shortcuts import render

# Create your views here.
import logging
import sys

from tutils import tconf
from tutils.t_global_data import TGlobalData
from video_manager.models import Tag, Video

reload(sys)
sys.setdefaultencoding('utf-8')


# 转发URL
def trans(request, url):
    s = ""
    try:
        # print "url:", url
        # 解码两遍URL
        url = urllib.unquote(url)
        logging.error("url1 : ----------------" + url)
        # url = urllib.unquote(url)
        # logging.info("url2 : " + url)
        s = urllib2.urlopen(url).read()
    except Exception, e:
        s = "转发URL异常:" + url
        print e
    finally:
        return HttpResponse(s)


def get_file(request, file_name):
    def file_iterator(file_name, chunk_size=512):
        print "file_name : ", file_name
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    the_file_name = TGlobalData.STATIC_RECV_PATH + file_name
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    return response


# 获取标签
def get_tags(request):
    s = ""
    try:
        all_tags = Tag.objects.all()
        response_data = []
        for item in all_tags:
            res_item = {}
            res_item['name'] = item.title
            res_item['desc'] = item.desc
            res_item['id'] = item.id
            response_data.append(res_item)
        s = json.dumps(response_data)
        s = eval("u" + "\'" + s + "\'")
    except Exception, e:
        s = "转发URL异常:", e
        print e
    finally:
        return HttpResponse(s)


# 获取标签
def get_video_by_tag(request, tag):
    s = ""
    try:
        all_videos = Video.objects.filter(id=tag)
        response_data = []
        for item in all_videos:
            res_item = {}
            res_item['title'] = item.title
            res_item['pic_url'] = urllib.unquote(item.pic_url.url)[len(TGlobalData.STATIC_RECV_PATH):]
            res_item['video_url'] = item.video_url
            res_item['desc'] = item.desc
            response_data.append(res_item)
        s = json.dumps(response_data)
        s = eval("u" + "\'" + s + "\'")
    except Exception, e:
        s = "转发URL异常:", e
        print e
    finally:
        return HttpResponse(s)
