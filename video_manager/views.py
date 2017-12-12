# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
import logging
import sys
import traceback

from django.http import HttpResponse, StreamingHttpResponse
from django.template.loader import get_template

import logic.people_manager
import logic.play_ctrl
import logic.video_ctrl
from tutils import t_url_tools
from tutils.t_global_data import TGlobalData
from video_manager.logic import video_ctrl, people_manager, play_ctrl, show_res

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


def lxdzx(request, action):
    print request.get_full_path()
    logging.debug(request.get_host() + " -- " + request.get_full_path())
    s = ""
    try:
        # 校验
        json_obj, session_res = t_url_tools.parse_url(request)
        if not session_res:
            s = t_url_tools.get_session_err_res()
            return

        if action == "get_tags":
            s = video_ctrl.get_tags(json_obj)
        elif action == "get_video_by_tag":
            s = video_ctrl.get_video_by_tag(json_obj)
        elif action == "get_video_by_gjz":
            s = video_ctrl.get_video_by_gjz(json_obj)
        elif action == "login":
            s = people_manager.login(json_obj)
        elif action == "play_video":
            s = play_ctrl.play_video(json_obj)
        elif action == "get_videos_oder":
            s = video_ctrl.get_videos_order(json_obj)
        elif action == "get_video_by_id":
            s = video_ctrl.get_video_by_id(json_obj)
        elif action == "add_play_record":
            s = play_ctrl.add_play_record(json_obj)
        elif action == "get_people_play_record":
            s = play_ctrl.get_people_play_record(json_obj)
        elif action == "do_my_fav":
            s = play_ctrl.do_my_fav(json_obj)
        elif action == "get_people_fav":
            s = play_ctrl.get_people_fav(json_obj)
        else:
            s = t_url_tools.get_response_str({}, success=False, msg="no " + action,
                                             err_code=t_url_tools.ERR_CODE_EXCEPTION)
    except Exception, e:
        traceback.print_exc()
        s = t_url_tools.get_response_str({}, success=False, msg=action + " 异常",
                                         err_code=t_url_tools.ERR_CODE_EXCEPTION)
    finally:
        print s
        logging.debug(s)
        return HttpResponse(s)


def lxdzx_show(request, action):
    print request.get_full_path()
    try:
        if action == "statistics_videos":
            s = show_res.statistics_videos(request)
    except Exception, e:
        traceback.print_exc()
        s = t_url_tools.get_response_str({}, success=False, msg=action + " 错误",
                                         err_code=t_url_tools.ERR_CODE_EXCEPTION)
    finally:
        print s
        logging.debug(s)
        return HttpResponse(s)


def add_video_comment(request):
    return logic.play_ctrl.add_video_comment(request)


def del_video_comment(request):
    return logic.play_ctrl.del_video_comment(request)


def get_video_comment(request):
    return logic.play_ctrl.get_video_comment(request)
