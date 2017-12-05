# -*- coding: utf-8 -*-

# 播放控制

import time
import traceback

from django.db.models import Count
from django.http import HttpResponse
from django.template.loader import get_template

from tutils import t_url_tools
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


def add_play_record(request):
    s = "[]"
    try:
        json_obj, session_res = t_url_tools.parse_url(request)
        if not session_res:
            s = t_url_tools.get_session_err_res()
            return

        vid = json_obj['vid']
        pid = json_obj['pid']

        video_rec = Video_Record()
        video_rec.video_id = Video.objects.filter(id=vid).first()
        video_rec.people_id = People.objects.filter(id=pid).first()
        video_rec.save()

        s = t_url_tools.get_response_str({})
    except Exception, e:
        traceback.print_exc()
        s = t_url_tools.get_response_str({}, success=False, msg="add_play_record 异常",
                                         err_code=t_url_tools.ERR_CODE_EXCEPTION)
    finally:
        return HttpResponse(s)


def get_people_play_record(request):
    s = "[]"
    try:
        json_obj, session_res = t_url_tools.parse_url(request)
        if not session_res:
            s = t_url_tools.get_session_err_res()
            return

        pid = json_obj['pid']
        people = People.objects.filter(id=pid).first()

        recs = Video_Record.objects.filter(people_id_id=pid).select_related('video_id').order_by("-watch_time")

        vids = []
        response_data = []
        for item in recs:
            if item.video_id.id in vids:
                continue
            else:
                vids.append(item.video_id.id)
            # print model_to_dict(item)
            # print item.video_id.title
            res_item = {'title': item.video_id.title}
            res_item['pic_url'] = t_url_tools.get_file_url(item.video_id.pic_url)[1]
            res_item['video_url'] = item.video_id.video_url
            res_item['desc'] = item.video_id.desc
            res_item['id'] = item.video_id.id
            res_item['watch_time'] = str(item.watch_time)[:str(item.watch_time).index(".")]
            response_data.append(res_item)
        s = t_url_tools.get_response_str(response_data)
    except Exception, e:
        traceback.print_exc()
        s = t_url_tools.get_response_str({}, success=False, msg="get_people_play_record 异常",
                                         err_code=t_url_tools.ERR_CODE_EXCEPTION)
    finally:
        return HttpResponse(s)


def do_my_fav(request):
    """
    控制我的收藏
    :param request:
    :return:
    """
    s = "[]"
    try:
        json_obj, session_res = t_url_tools.parse_url(request)
        if not session_res:
            s = t_url_tools.get_session_err_res()
            return

        vid = json_obj['vid']
        pid = json_obj['pid']

        s = ""
        pf = People_Favorite.objects.filter(video_id_id=vid).filter(people_id_id=pid).first()
        if pf is None:
            pf_new = People_Favorite()
            pf_new.video_id = Video.objects.filter(id=vid).first()
            pf_new.people_id = People.objects.filter(id=pid).first()
            pf_new.save()
            s = "添加收藏成功"
        else:
            pf.delete()
            s = "删除收藏成功"
        s = t_url_tools.get_response_str({'res': s})
    except Exception, e:
        traceback.print_exc()
        s = t_url_tools.get_response_str({}, success=False, msg="do_my_fav 异常",
                                         err_code=t_url_tools.ERR_CODE_EXCEPTION)
    finally:
        return HttpResponse(s)


def get_people_fav(request):
    s = "[]"
    try:
        json_obj, session_res = t_url_tools.parse_url(request)
        if not session_res:
            s = t_url_tools.get_session_err_res()
            return
        pid = int(json_obj['pid'])
        vid = int(json_obj['vid'])

        if vid > 0:
            recs = People_Favorite.objects.filter(people_id_id=pid, video_id_id=vid).select_related('video_id')
        else:
            recs = People_Favorite.objects.filter(people_id_id=pid).select_related('video_id')

        response_data = []
        for item in recs:
            # print model_to_dict(item)
            # print item.video_id.title
            res_item = {'title': item.video_id.title}
            res_item['pic_url'] = t_url_tools.get_file_url(item.video_id.pic_url)[1]
            res_item['video_url'] = item.video_id.video_url
            res_item['desc'] = item.video_id.desc
            res_item['id'] = item.video_id.id
            response_data.append(res_item)
        s = t_url_tools.get_response_str(response_data)
    except Exception, e:
        traceback.print_exc()
        s = t_url_tools.get_response_str({}, success=False, msg="get_people_fav 异常",
                                         err_code=t_url_tools.ERR_CODE_EXCEPTION)
    finally:
        return HttpResponse(s)


class Video_Statistics_Model:
    def __init__(self, title, count, video):
        self.title = title
        self.count = count
        self.video = video


# 视频播放量
def statistics_videos(request):
    """
    播放量
    :param request:
    :return:
    """
    s = "[]"
    try:
        json_obj, session_res = t_url_tools.parse_url(request)
        recs = Video_Record.objects.values_list('video_id').annotate(Count('video_id'))

        response_data = []
        for item in recs:
            video = Video.objects.filter(id=item[0]).first()
            count = item[1]
            video.play_count = count
            video.save()
            res_item = Video_Statistics_Model(video.title, count, video)  # {'video': video, "count": count}
            response_data.append(res_item)
        t = get_template('statistics.html')
        s = t.render({'res': response_data})
    except Exception, e:
        traceback.print_exc()
        s = t_url_tools.get_response_str({}, success=False, msg="statistics_videos 异常",
                                         err_code=t_url_tools.ERR_CODE_EXCEPTION)
    finally:
        return HttpResponse(s)
