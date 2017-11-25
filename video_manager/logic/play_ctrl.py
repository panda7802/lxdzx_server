# -*- coding: utf-8 -*-

# 播放控制

import traceback

from django.http import HttpResponse, StreamingHttpResponse
from django.template.loader import get_template

from tutils import t_url_tools
from tutils.t_global_data import TGlobalData
from video_manager.models import *


def play_video(request):
    s = "[]"
    try:
        json_obj, session_res = t_url_tools.parse_url(request)
        if not session_res:
            s = t_url_tools.get_session_err_res()
            return

        vid = json_obj['vid']
        pid = json_obj['pid']
        all_videos = Video.objects.filter(id=vid)
        if all_videos.__len__() <= 0:
            s = t_url_tools.get_response_str({}, success=False, msg="视频不存在", err_code=t_url_tools.ERR_CODE_DATA)
            return

        all_peoples = People.objects.filter(id=pid)
        if all_peoples.__len__() <= 0:
            s = t_url_tools.get_response_str({}, success=False, msg="个人信息有误，请重新登录", err_code=t_url_tools.ERR_CODE_DATA)
            return

        video_recod = Video_Record()
        video_recod.video_id = all_videos.first()
        video_recod.people_id = all_peoples.first()
        video_recod.save()

        # 记录播放量
        video_model = all_videos.first()
        play_count = video_model.play_count
        video_model.play_count = play_count + 1
        video_model.save()

        s = t_url_tools.get_response_str({})
    except Exception, e:
        traceback.print_exc()
        s = t_url_tools.get_response_str({}, success=False, msg="play_video 异常",
                                         err_code=t_url_tools.ERR_CODE_EXCEPTION)
    finally:
        return HttpResponse(s)
