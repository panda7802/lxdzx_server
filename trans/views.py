# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import logging
import traceback
import urllib
import urllib2
from json import JSONDecoder

from django.http import HttpResponse
import sys

from django.template.loader import get_template

reload(sys)
sys.setdefaultencoding('utf-8')


# 转发URL
def trans_url(request, url):
    s = ""
    try:
        # 解码两遍URL
        logging.debug(request.get_host() + " -- " + request.get_full_path())
        python_obj = JSONDecoder().decode(url)
        url = urllib.unquote(python_obj['url'])
        url = url.replace("tnbhh.cn","lai4.com.cn")
        logging.debug("trans url : " + url)
        s = urllib2.urlopen(url).read()
    except Exception, e:
        s = "转发URL异常:" + url
        print traceback.format_exc()
    finally:
        return HttpResponse(s)


# 给孙子演示用的
def t_car_check(request, action):
    page = 'show4grandson/' + action + '.html'
    t = get_template(page)
    s = t.render()
    return HttpResponse(s)


# 年会
def t_nh(request, action):
    page = 'nh/' + action + '.html'
    t = get_template(page)
    s = t.render()
    return HttpResponse(s)
