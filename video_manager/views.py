# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
import sys
import traceback

from django.http import HttpResponse, StreamingHttpResponse
from django.template.loader import get_template

from tutils import t_url_tools
from tutils.t_global_data import TGlobalData
from video_manager.models import Tag, Video, People

import logic.people_manager
import logic.video_ctrl
import logic.play_ctrl

reload(sys)
sys.setdefaultencoding('utf-8')


# Create your views here.
def t_index(request):
    t = get_template('index.html')
    s = t.render()
    return HttpResponse(s)


# Create your views here.
def t_home_page(request):
    t = get_template('cpJC9PX6Nu.txt')
    s = t.render()
    return HttpResponse(s)


# 获取文件
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
    return logic.video_ctrl.get_tags(request)


# 通过标签获取视频
def get_video_by_tag(request):
    return logic.video_ctrl.get_video_by_tag(request)


# 通过关键字搜索视频
def get_video_by_gjz(request):
    return logic.video_ctrl.get_video_by_gjz(request)


# 登录
def login(request):
    return logic.people_manager.login(request)


# 播放视频
def play_video(request):
    return logic.play_ctrl.play_video(request)


#根据id获取视频
def get_video_by_id(request):
    return logic.video_ctrl.get_video_by_id(request)

# 排序视频
def get_videos_order(request):
    return logic.video_ctrl.get_videos_order(request)




# TODO 欢迎页
