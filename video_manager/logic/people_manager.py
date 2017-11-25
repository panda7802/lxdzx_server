# -*- coding: utf-8 -*-

#人员管理

import traceback

from django.http import HttpResponse, StreamingHttpResponse
from django.template.loader import get_template

from tutils import t_url_tools
from tutils.t_global_data import TGlobalData
from video_manager.models import Tag, Video, People


def login(request):
    s = "[]"
    try:
        json_obj, session_res = t_url_tools.parse_url(request, is_check_session=False)
        wx_name = json_obj['wx_name']
        # people = People.objects.filter(wx=gjz)
        people = People.objects.filter(wx_name=wx_name)
        people_count = people.__len__()
        if people_count > 0:
            people_id = people[0].id
        else:
            people = People()
            people.wx_name = wx_name
            people.save()
            people_id = people.id
        res = {"id": people_id}
        s = t_url_tools.get_response_str(res)
    except Exception, e:
        traceback.print_exc()
        s = "get_video_by_gjz异常:", e
    finally:
        return HttpResponse(s)
