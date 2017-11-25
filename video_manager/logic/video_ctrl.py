# -*- coding: utf-8 -*-

# 视频管理

import traceback

from django.http import HttpResponse, StreamingHttpResponse
from django.template.loader import get_template

from tutils import t_url_tools
from tutils.t_global_data import TGlobalData
from video_manager.models import Tag, Video, People


# 获取标签
def get_tags(request):
    s = ""
    try:
        t_url_tools.parse_url(request, False)

        all_tags = Tag.objects.all()
        response_data = []
        for item in all_tags:
            res_item = {'name': item.title}
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

        tag = json_obj['tag']
        page = json_obj['page']
        rows = json_obj['rows']

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
        all_videos = Video.objects.filter(title__contains=gjz)
        response_data = []
        for item in all_videos:
            res_item = {'title': item.title}
            res_item['pic_url'] = t_url_tools.get_file_url(item.pic_url)[1]
            res_item['video_url'] = item.video_url
            res_item['desc'] = item.desc
            response_data.append(res_item)
        s = t_url_tools.get_response_str(response_data)
    except Exception, e:
        traceback.print_exc()
        # s = "get_video_by_gjz异常:", e
        s = t_url_tools.get_response_str({}, success=False, msg="get_video_by_gjz 异常",
                                         err_code=t_url_tools.ERR_CODE_EXCEPTION)
    finally:
        return HttpResponse(s)
