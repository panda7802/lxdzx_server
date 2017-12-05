# -*- coding: utf-8 -*-

# 视频管理

import traceback

from django.http import HttpResponse, StreamingHttpResponse
from django.template.loader import get_template
from django.db.models import Q

from tutils import t_url_tools
from tutils.t_global_data import TGlobalData
from video_manager.models import Tag, Video, People


# 获取标签
def get_tags(request):
    s = ""
    try:
        # http: // 127.0 .0.1:8000 / get_tags?parm = {"tag": 1}
        json_obj, session_res = t_url_tools.parse_url(request)
        if not session_res:
            s = t_url_tools.get_session_err_res()
            return

        tag = int(json_obj['tag'])
        if tag < 0:
            all_tags = Tag.objects.all()
        else:
            all_tags = Tag.objects.filter(parent_tag_id=tag)
        response_data = []
        for item in all_tags:
            res_item = {}
            res_item['pic_url'] = t_url_tools.get_file_url(item.pic_url)[1]
            res_item['title'] = item.title
            res_item['desc'] = item.desc
            res_item['id'] = item.id
            response_data.append(res_item)
        s = t_url_tools.get_response_str(response_data)
    except Exception, e:
        # s = "get_tags异常:", e
        traceback.print_exc()
        s = t_url_tools.get_response_str({}, success=False, msg="get_tags 异常",
                                         err_code=t_url_tools.ERR_CODE_EXCEPTION)
    finally:
        return HttpResponse(s)


# 通过标签获取视频
def get_video_by_tag(request):
    s = "[]"
    try:
        json_obj, session_res = t_url_tools.parse_url(request)
        if not session_res:
            s = t_url_tools.get_session_err_res()
            return

        tag = int(json_obj['tag'])
        page = int(json_obj['page'])
        rows = int(json_obj['rows'])

        # 在没有manyToMany的表里面
        search_tag = Tag.objects.filter(id=tag).first()
        if None == search_tag:
            return HttpResponse(s)

        all_videos = search_tag.video_set.all()[page:rows + page]
        response_data = []
        for item in all_videos:
            res_item = {'title': item.title}
            res_item['pic_url'] = t_url_tools.get_file_url(item.pic_url)[1]
            res_item['video_url'] = item.video_url
            res_item['desc'] = item.desc
            res_item['id'] = item.id
            response_data.append(res_item)
        s = t_url_tools.get_response_str(response_data)
    except Exception, e:
        traceback.print_exc()
        # s = "get_video_by_tag异常:", e
        s = t_url_tools.get_response_str({}, success=False, msg="get_video_by_tag 异常",
                                         err_code=t_url_tools.ERR_CODE_EXCEPTION)
    finally:
        return HttpResponse(s)


# 通过关键字搜索视频
def get_video_by_gjz(request):
    s = "[]"
    try:
        json_obj, session_res = t_url_tools.parse_url(request)
        if not session_res:
            s = t_url_tools.get_session_err_res()
            return

        gjz = json_obj['gjz']
        all_videos = Video.objects.filter(Q(title__contains=gjz) | Q(desc__contains=gjz))
        response_data = []
        for item in all_videos:
            res_item = {'title': item.title}
            res_item['pic_url'] = t_url_tools.get_file_url(item.pic_url)[1]
            res_item['video_url'] = item.video_url
            res_item['desc'] = item.desc
            res_item['id'] = item.id
            response_data.append(res_item)
        s = t_url_tools.get_response_str(response_data)
    except Exception, e:
        traceback.print_exc()
        # s = "get_video_by_gjz异常:", e
        s = t_url_tools.get_response_str({}, success=False, msg="get_video_by_gjz 异常",
                                         err_code=t_url_tools.ERR_CODE_EXCEPTION)
    finally:
        return HttpResponse(s)


# 排序视频
def get_videos_order(request):
    s = "[]"
    try:
        json_obj, session_res = t_url_tools.parse_url(request)
        if not session_res:
            s = t_url_tools.get_session_err_res()
            return

        video_type = int(json_obj['type'])
        page = int(json_obj['page'])
        rows = int(json_obj['rows'])
        all_videos = []
        if 1 == video_type:  # 最新
            all_videos = Video.objects.order_by("-upload_time")[page:rows + page]
        elif 2 == video_type:  # 最热
            all_videos = Video.objects.order_by("-play_count")[page:rows + page]
        elif 3 == video_type:  # 推荐
            all_videos = Video.objects.order_by("-recommend")[page:rows + page]
        else:
            s = t_url_tools.get_response_str({}, success=False, msg="查找类型有误",
                                             err_code=t_url_tools.ERR_CODE_PARM)
        response_data = []
        for item in all_videos:
            res_item = {'title': item.title}
            res_item['pic_url'] = t_url_tools.get_file_url(item.pic_url)[1]
            res_item['video_url'] = item.video_url
            res_item['desc'] = item.desc
            res_item['id'] = item.id
            response_data.append(res_item)
        s = t_url_tools.get_response_str(response_data)
    except Exception, e:
        traceback.print_exc()
        # s = "get_video_by_gjz异常:", e
        s = t_url_tools.get_response_str({}, success=False, msg="get_videos_order 异常",
                                         err_code=t_url_tools.ERR_CODE_EXCEPTION)
    finally:
        return HttpResponse(s)


def get_video_by_id(request):
    s = "[]"
    try:
        json_obj, session_res = t_url_tools.parse_url(request)
        if not session_res:
            s = t_url_tools.get_session_err_res()
            return

        vid = json_obj['vid']
        all_videos = Video.objects.filter(id=vid)
        if all_videos.__len__() <= 0:
            s = t_url_tools.get_response_str({}, success=False, msg="视频不存在", err_code=t_url_tools.ERR_CODE_DATA)
            return

        # 记录播放量
        video_model = all_videos.first()
        res_item = {'title': video_model.title}
        res_item['pic_url'] = t_url_tools.get_file_url(video_model.pic_url)[1]
        res_item['video_url'] = video_model.video_url
        res_item['desc'] = video_model.desc
        res_item['id'] = video_model.id
        s = t_url_tools.get_response_str(res_item)
    except Exception, e:
        traceback.print_exc()
        s = t_url_tools.get_response_str({}, success=False, msg="play_video 异常",
                                         err_code=t_url_tools.ERR_CODE_EXCEPTION)
    finally:
        return HttpResponse(s)


