# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import traceback

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from get_web_data.models import PlatformStatistics, VideoNameInfos
from tutils import t_url_tools


def get_dgtj(request, action):
    logging.debug(request.get_full_path())
    s = "[]"
    try:
        json_obj, session_res = t_url_tools.parse_url(request, is_check_session=False)
        if not session_res:
            s = t_url_tools.get_session_err_res()
            return
        svid = json_obj['vid']
        vids = svid.split(",")
        response_data = []
        s = ""
        for vid in vids:
            item = PlatformStatistics.objects.filter(vid_id=vid).first()
            # res_item = {'name': item.vid.name}
            res_item = {
                'name': filter(lambda t: t[0] == item.vid.platform, VideoNameInfos.PLATFORM_SIDES)[0][1]}
            res_item['clicks'] = item.clicks
            res_item['fans'] = item.fans
            res_item['follows'] = item.follows
            res_item['reads'] = item.reads
            response_data.append(res_item)
            # s = "平台：",res_item['name'],"点击量：" ,res_item['clicks'] ,""
            sitem = "平台 ： %s\t\t  , 点击量：%s ，粉丝数：%s，关注数:%s ，阅读数:%s  <Br/>" % \
                    (res_item['name'], res_item['clicks'], res_item['fans'], res_item['follows'], res_item['reads'])
            s = s + sitem
            # s = t_url_tools.get_response_str(response_data)
    except Exception, e:
        traceback.print_exc()
        s = t_url_tools.get_response_str({}, success=False, msg="get_dgtj 异常",
                                         err_code=t_url_tools.ERR_CODE_EXCEPTION)
    finally:
        return HttpResponse(s)
