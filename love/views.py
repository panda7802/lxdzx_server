# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template

reload(sys)
sys.setdefaultencoding('utf-8')


def love_index(request):
    t = get_template('love/love_index.html')
    show_data = {'res': [
        {'title': "第一次微信聊天", "desc": "我说：\"您好\"", "time": "2016-03-29 20:45"},
        {'title': "第一次见面", "desc": "你说：\"你是姓潘吧\"", "time": "2017-04-09 11:45"},
        {'title': "第一次看电影", "desc": "看得是愤怒的小鸟", "time": "2017-05-21 15:10"},
        {'title': "表白", "desc": "在天之都大厦门口", "time": "2017-05-21 20:15"},
        {'title': "牵手", "desc": "用得是过马路法则", "time": "2017-05-28 17:30"},
    ]}
    s = t.render(show_data)
    return HttpResponse(s)
