# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import urllib
import urllib2

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.

# 转发URL
def trans(request, url):
    s = ""
    try:
        print "url:", url
        #解码两遍URL
        url = urllib.unquote(url)
        url = urllib.unquote(url)
        s = urllib2.urlopen(url).read()
    except Exception, e:
        s = "转发URL异常:" + url
#        print e
        s = str(e)
    finally:
        return HttpResponse(s)
