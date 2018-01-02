# -*- coding: utf-8 -*-

# 视频管理
import hashlib
import json

import time
import urllib
from json import JSONDecoder

from django.template.loader import get_template
import logging

from tutils import t_url_tools
from video_manager.models import People, Xnjy


def xnjy_save_xnjy(json_obj):
    # 增加微信名称
    nick_name = json_obj['nick_name']
    people = People.objects.filter(name=nick_name)
 #   people_count = people.__len__()
    people_count = 0
    if people_count <= 0:
        people = People()
        people.name = nick_name
        people.save()
 #       people = People.objects.filter(name=nick_name).first()
    else:
        people = people.first()

    xnjy = Xnjy.objects.filter(people_id=people).first()
    if xnjy is None:
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
    nick_name = json_obj['nick_name']
    people = People.objects.filter(name=nick_name).first()
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



def xnjy_index1(request):
    """
    新年寄语
    :param request:
    :return:
    """
    ui_type = 1
    try:
        json_obj, session_res = t_url_tools.parse_url(request)
        ui_type = int(json_obj['ui_type'])
    except Exception, e:
        pass

    if 1 == ui_type:
        ui_type = "yellow"
    else:
        ui_type = "blue"

    t = get_template('xnjy/index1.html')
    s = t.render({'ui_type': ui_type})
    return s


def xnjy_index(request):
    """
    新年寄语
    :param request:
    :return:
    """
    ui_type = 1
    try:
        json_obj, session_res = t_url_tools.parse_url(request)
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

    ui_type = 1
    try:
        json_obj, session_res = t_url_tools.parse_url(request)
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

    xnjy = Xnjy.objects.filter(people_id__name=wx_name).first()
    if xnjy is None:
        xnjy = Xnjy()
    t = get_template('xnjy/input.html')
    s = t.render({'xnjy': xnjy, 'ui_type': ui_type})
    return s


def xnjy_show(request):
    """
    新年寄语
    :param request:
    :return:
    """

    json_obj, session_res = t_url_tools.parse_url(request)
    ui_type = 1
    try:
        ui_type = int(json_obj['ui_type'])
    except Exception, e:
        pass

    if 1 == ui_type:
        ui_type = "yellow"
    else:
        ui_type = "blue"
    nick_name = ""
    try:
        nick_name = json_obj['nick_name']
    except Exception, e:
        pass

    xnjy = Xnjy.objects.filter(people_id__name=nick_name).first()
    if xnjy is None:
        print xnjy
        xnjy = Xnjy()
    # t = get_template('xnjy/input.html')
    # s = t.render({'xnjy': xnjy, 'ui_type': ui_type})

    t = get_template('xnjy/show.html')
    s = t.render({'xnjy': xnjy, 'ui_type': ui_type})
    return s


import urllib2


def xnjy_gzh(request):
    ui_type = 0
    try:
        json_obj, session_res = t_url_tools.parse_url(request)
        ui_type = int(json_obj['ui_type'])
    except Exception, e:
        pass

    url = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxaa3e9bee4d1d172d&redirect_uri=https%3a%2f%2fwww.pandafly.cn%2flxdzx_show%2fxnjy_gzh&response_type=code&scope=snsapi_base&state=123#wechat_redirect"
    res = urllib2.urlopen(url).read()
    logging.debug("xnjy_gzh : " + res)

    # s = t.render({'xnjy': xnjy, 'ui_type': ui_type})
    #   s = "panguotian"
    s = res
    return s


def getAccessToken(appId, appSecret):
    s = ""
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=" + appId + "&secret=" + appSecret
    print "getAccessToken : ", url
    temp = urllib2.urlopen(url).read()
    try:
        logging.debug("temp : " + temp)
        json_obj = JSONDecoder().decode(temp)
        s = json_obj['access_token']
    except Exception, e:
        logging.exception(e)
 #   s = "5_1eJMj69V1nkvNxQ43JucLyFPVT2enc8YpDYItW_vCK7OTCxAoU2XrL8DpHI3EMx5vP1syau9iLz08kQCAwCOeViEpqvKOmzJKm8RXha17sbaGttSs3NCNcZ2nPG005gpS8wldTxSBJpxSIaqWPQeABAIBC"
    return s


def get_jsapi_ticket(accessToken):
    s = ""
    url = "https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token=" + accessToken + "&type=jsapi"
    logging.debug("get_jsapi_ticket : ", url)
    temp = urllib2.urlopen(url).read()
    try:
        logging.debug("temp : " + temp)
        json_obj = JSONDecoder().decode(temp)
        s = json_obj['ticket']
    except Exception, e:
        logging.exception(e)
    return s


def get_sing(url, timeStamp, nonceStr, appId='wxaa3e9bee4d1d172d', appSecret='d0a7b8b491c15da6e3670da3d142495e'):
#def get_sing(url, timeStamp, nonceStr, appId='wx29db0e2cd630f115', appSecret='8893b55244bd1c64e25c45fde5973cda'):
    access_token = getAccessToken(appId, appSecret)
    jsapi_ticket = get_jsapi_ticket(access_token)
    logging.debug("accessToken : " + access_token)
    logging.debug("jsapi_ticket : " + jsapi_ticket)
    sign_value = "jsapi_ticket=" + jsapi_ticket + "&noncestr=" + nonceStr + "&timestamp=" + timeStamp + "&url=" + url;
    logging.debug("微信JS-SDK权限验证的签名串：" + sign_value)
    # 这个签名.主要是给加载微信js使用.别和上面的搞混了.
    signature = hashlib.sha1(sign_value).hexdigest()
    logging.debug("微信JS-SDK权限验证的签名：" + signature)
    s = signature
    return s


def xnjy_share(request):
    logging.debug(request.get_full_path())
    timeStamp = "1414587457"  # str(time.time())
    nonceStr = "panguotian"
    url = request.GET.get("url")
    url = urllib.unquote(url)
    res = {}
    res['timeStamp'] = timeStamp
    res['nonceStr'] = nonceStr
    res['url'] = url
    res['signature'] = get_sing(url, timeStamp, nonceStr)
    s = json.dumps(res)
    return s


