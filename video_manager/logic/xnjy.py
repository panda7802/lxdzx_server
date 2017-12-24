# -*- coding: utf-8 -*-

# 视频管理

from django.template.loader import get_template

from tutils import t_url_tools
from video_manager.models import People, Xnjy


def xnjy_save_xnjy(json_obj):
    # 增加微信名称
    wx_name = json_obj['wx_name']
    people = People.objects.filter(wx_name=wx_name)
    people_count = people.__len__()
    if people_count <= 0:
        people = People()
        people.wx_name = wx_name
        people.save()
        people = People.objects.filter(wx_name=wx_name).first()
    else:
        people = people.first()

    xnjy = Xnjy.objects.filter(people_id=people)
    if xnjy.__len__() <= 0:
        xnjy = Xnjy()
    xnjy.school = json_obj['school']
    xnjy.jy = json_obj['jy']
    xnjy.lx_time = json_obj['lx_time']
    xnjy.people_id = people
    xnjy.save()
    # res = {"id": people_id}
    s = t_url_tools.get_response_str({})
    return s


def xnjy_get_xnjy(json_obj):
    # 增加微信名称
    wx_name = json_obj['wx_name']
    people = People.objects.filter(wx_name=wx_name).first()
    res_item = {'school': ""}
    res_item['jy'] = ""
    res_item['lx_time'] = ""
    if people is not None:
        xnjy = Xnjy.objects.filter(people_id=people).first()
        if xnjy is not None:
            res_item = {'school': xnjy.school}
            res_item['jy'] = xnjy.jy
            res_item['lx_time'] = xnjy.lx_time
    # res = {"id": people_id}
    s = t_url_tools.get_response_str({'res': res_item})
    return s


def xnjy_index(request):
    """
    新年寄语
    :param request:
    :return:
    """

    json_obj, session_res = t_url_tools.parse_url(request)
    ui_type = 0
    try:
        ui_type = int(json_obj['ui_type'])
    except Exception, e:
        pass

    if 1 == ui_type:
        ui_type = "yellow"
    else:
        ui_type = "blue"

    t = get_template('xnjy/index.html')
    s = t.render({'ui_type': ui_type})
    return s


def xnjy_input(request):
    """
    新年寄语 录入
    :param request:
    :return:
    """

    json_obj, session_res = t_url_tools.parse_url(request)
    ui_type = 0
    try:
        ui_type = int(json_obj['ui_type'])
    except Exception, e:
        pass

    if 1 == ui_type:
        ui_type = "yellow"
    else:
        ui_type = "blue"

    wx_name = ""
    try:
        wx_name = json_obj['wx_name']
    except Exception, e:
        pass

    xnjy = Xnjy.objects.filter(people_id__wx_name=wx_name).first()
    if xnjy is None:
        xnjy = Xnjy()
    t = get_template('xnjy/input.html')
    s = t.render({'xnjy': xnjy})
    return s


def xnjy_show(request):
    """
    新年寄语
    :param request:
    :return:
    """

    json_obj, session_res = t_url_tools.parse_url(request)
    ui_type = 0
    try:
        int(json_obj['ui_type'])
    except Exception, e:
        pass

    if 1 == ui_type:
        ui_type = "yellow"
    else:
        ui_type = "blue"

    t = get_template('xnjy/index.html')
    s = t.render({'ui_type': ui_type})
    return s
