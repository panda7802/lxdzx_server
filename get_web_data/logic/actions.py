# coding=utf-8


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import traceback

import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template

from get_web_data.models import PlatformStatistics, VideoNameInfos
from tutils import t_url_tools


def get_dgtj(json_obj):
    s = "[]"
    # json_obj, session_res = t_url_tools.parse_url(request, is_check_session=False)
    # if not session_res:
    #     s = t_url_tools.get_session_err_res()
    #     return
    svid = json_obj['vid']
    # svid = "2,3"
    vids = svid.split(",")
    response_data = []
    s = ""
    for vid in vids:
        item = PlatformStatistics.objects.filter(vid_id=vid).first()
        # res_item = {'name': item.vid.name}
        res_item = {'name': filter(lambda t: t[0] == item.vid.platform, VideoNameInfos.PLATFORM_SIDES)[0][1],
                    'clicks': item.clicks, 'fans': item.fans, 'follows': item.follows, 'reads': item.reads}
        response_data.append(res_item)
        # s = "平台：",res_item['name'],"点击量：" ,res_item['clicks'] ,""
        sitem = "平台 ： %s\t\t  , 点击量：%s ，粉丝数：%s，关注数:%s ，阅读数:%s  <Br/>" % \
                (res_item['name'], res_item['clicks'], res_item['fans'], res_item['follows'], res_item['reads'])
        s = s + sitem
    return s


def get_dgtj_echart(json_obj):
    s = "{}"
    vid = json_obj['vid']
    svid = json_obj['vid']
    vids = svid.split(",")

    # 目标平台
    obj_platforms = VideoNameInfos.objects.filter(get_data=0, id__in=vids)
    obj_platforms_names = []
    for item in obj_platforms:
        obj_platforms_names.append(
            filter(lambda platform_ids: platform_ids[0] == item.platform, VideoNameInfos.PLATFORM_SIDES)[0][1])

    # 点击量,关注数等
    get_obj = []
    # start = datetime.datetime.now() - datetime.timedelta(hours=0, minutes=59, seconds=59)
    start_time = datetime.datetime.strptime("20180907200000", "%Y%m%d%H%M%S")
    end_time = datetime.datetime.strptime("20180908200000", "%Y%m%d%H%M%S")
    datas = []
    s_times = ""
    get_time_over = False
    for index, vid in enumerate(vids):
        data = {"name": obj_platforms_names[index]}
        s_num = ""
        tmp_time = start_time
        last_num = -1
        while tmp_time <= end_time:
            if False == get_time_over:
                s_times += tmp_time.strftime("%m-%d", tmp_time)
            item = PlatformStatistics.objects.filter(get_time__gte=tmp_time, vid_id=vid).order_by("get_time").first()
            if last_num >= 0:
                min_num = item.clicks - last_num
                s_num += str(min_num) + ","
            last_num = item.clicks
            # logging.debug(str(item) + ", " + str(item.get_time))
            logging.debug(str(data) + ", " + str(s_num))
            tmp_time = tmp_time + datetime.timedelta(hours=1)
        get_time_over = True

    # 显示
    t = get_template('get_web_data/get_fans_add.html')
    show_data = {'obj_platforms_names': obj_platforms_names, "get_time_over": get_time_over}

    s = t.render(show_data)
    return s
