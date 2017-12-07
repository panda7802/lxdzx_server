# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
import sys

from django.http import HttpResponse, StreamingHttpResponse
from django.template.loader import get_template

import logic.people_manager
import logic.play_ctrl
import logic.video_ctrl
from tutils.t_global_data import TGlobalData

reload(sys)
sys.setdefaultencoding('utf-8')


# Create your views here.
def t_index(request):
    t = get_template('index.html')
    s = t.render()
    return HttpResponse(s)


def notice(request):
    t = get_template('notice.html')
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


# 根据id获取视频
def get_video_by_id(request):
    return logic.video_ctrl.get_video_by_id(request)


# 排序视频
def get_videos_order(request):
    return logic.video_ctrl.get_videos_order(request)


# 增加播放记录
def add_play_record(request):
    return logic.play_ctrl.add_play_record(request)


def get_people_play_record(request):
    return logic.play_ctrl.get_people_play_record(request)


def do_my_fav(request):
    """
    删减我的收藏
    :param request:
    :return:
    """
    return logic.play_ctrl.do_my_fav(request)


def get_people_fav(request):
    """
    获取是否收藏
    :param request:
    :return:
    """
    return logic.play_ctrl.get_people_fav(request)


# TODO 获取欢迎页面URL

# TODO 记录播放进度

# TODO 统计视频播放量（UI），包括每个视频的播放时间
def statistics_videos(request):
    return logic.play_ctrl.statistics_videos(request)


def add_video_comment(request):
    return logic.play_ctrl.add_video_comment(request)


def del_video_comment(request):
    return logic.play_ctrl.del_video_comment(request)


def get_video_comment(request):
    return logic.play_ctrl.get_video_comment(request)


