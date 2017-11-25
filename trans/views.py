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
        python_obj = JSONDecoder().decode(url)
        url = urllib.unquote(python_obj['url'])
        s = urllib2.urlopen(url).read()
    except Exception, e:
        s = "转发URL异常:" + url
        print traceback.format_exc()
    finally:
        return HttpResponse(s)
