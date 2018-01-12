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
    # show_data = {'res': [
    #     {'title': "第一次微信聊天", "desc": "我说：\"您好\"", "time": "2016-03-29 20:45"},
    #     {'title': "第一次见面", "desc": "你说：\"你是姓潘吧\"", "time": "2017-04-09 11:45"},
    #     {'title': "第一次看电影", "desc": "看得是愤怒的小鸟", "time": "2017-05-21 15:10"},
    #     {'title': "表白", "desc": "在天之都大厦门口", "time": "2017-05-21 20:15"},
    #     {'title': "牵手", "desc": "用得是过马路法则", "time": "2017-05-28 17:30"},
    # ]}
    items = [
        {'title': "第一次微信聊天", "desc": "我说：“您好”", "time": "2016-03-29 20:45:43"},
        {'title': "第一次见面", "desc": "你说：“你是姓潘吧”", "time": "2016-04-09 11:45:54"},
        {'title': "第一次看电影", "desc": "看得是愤怒的小鸟", "time": "2016-05-21 15:10:13"},
        {'title': "表白", "desc": "在天之都大厦门口", "time": "2016-05-21 20:15:02"},
        {'title': "牵手", "desc": "用得是过马路法则", "time": "2016-05-28 17:30:32"},
        {'title': "第一次过情人节", "desc": "在七夕", "time": "2016-08-09 18:30:43"},
        {'title': "第一次见家长", "desc": "我提心吊胆", "time": "2016-09-16 17:30:23"},
        {'title': "谈婚论嫁", "desc": "你说：“好的”", "time": "2016-11-27 18:10:43"},
        {'title': "第一次见我父母", "desc": "我手心冒汗", "time": "2017-01-30 11:30:56"},
        {'title': "第一次回你老家", "desc": "你爸说我很内向", "time": "2017-02-20 17:30:41"},
        {'title': "第一次旅游", "desc": "在杭州", "time": "2017-05-20 09:30:56"},
        {'title': "第一次双方高层会晤", "desc": "很顺利！", "time": "2017-11-18 11:50:32"},
        {'title': "买婚戒", "desc": "你说“这个太大了，上班不方便”", "time": "2017-12-10 18:10:41"},
    ]
    show_data = {'res': items, 'len': items.__len__()}
    s = t.render(show_data)
    return HttpResponse(s)
