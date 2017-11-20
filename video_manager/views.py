# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
# Create your views here.
import sys
import traceback
import urllib

from django.http import HttpResponse, StreamingHttpResponse

from tutils.t_global_data import TGlobalData
from video_manager.models import Tag

reload(sys)
sys.setdefaultencoding('utf-8')


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
        res = {'success': True, 'msg': ""}
        response_data = []
        for item in all_tags:
            res_item = {'name': item.title}
            pic_url = urllib.unquote(item.pic_url.url).replace("\\", "/")
            res_item['pic_url'] = pic_url[pic_url.rindex("/") + 1:]
            res_item['title'] = item.title
            res_item['desc'] = item.desc
            res_item['id'] = item.id
            response_data.append(res_item)
        res['data'] = response_data
        s = json.dumps(res)
        s = eval("u" + "\'" + s + "\'")
    except Exception, e:
        s = "转发URL异常:", e
        print e
    finally:
        return HttpResponse(s)


# 获取标签
def get_video_by_tag(request, tag):
    s = "[]"
    try:
        # 在没有manyToMany的表里面
        search_tag = Tag.objects.filter(id=tag).first()
        res = {'success': True, 'msg': ""}
        if None == search_tag:
            return HttpResponse(s)

        all_videos = search_tag.video_set.all()
        response_data = []
        for item in all_videos:
            res_item = {'title': item.title}
            pic_url = urllib.unquote(item.pic_url.url).replace("\\", "/")
            res_item['pic_url'] = pic_url[pic_url.rindex("/") + 1:]
            res_item['video_url'] = item.video_url
            res_item['desc'] = item.desc
            response_data.append(res_item)
        res['data'] = response_data
        s = json.dumps(res)
        s = eval("u" + "\'" + s + "\'")
    except Exception, e:
        s = "转发URL异常:", e
        print traceback.print_exc()
    finally:
        return HttpResponse(s)
