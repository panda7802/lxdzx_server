# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class VideoList(models.Model):
    title = models.CharField(max_length=255)  # 标题
    subtitle = models.CharField(max_length=255)  # 子标题
    comment = models.CharField(max_length=255)  # 评论数
    created = models.CharField(max_length=255)  # 创建时间
    video_review = models.CharField(max_length=255)  # 弹幕数
    favorites = models.CharField(max_length=255)  # 收藏量
    length = models.CharField(max_length=255)  # 长度
    play = models.CharField(max_length=255)  # 播放量
    author = models.CharField(max_length=255)  # 作者
    review = models.CharField(max_length=255)
    typeid = models.CharField(max_length=255)  # 类型
    pic = models.CharField(max_length=255)  # 图片
    description = models.CharField(max_length=255)  # 描述
    aid = models.CharField(max_length=255)  # 详细信息id
    mid = models.CharField(max_length=255)  # 当前id
    copyright = models.CharField(max_length=255)  # 版权
    hide_click = models.CharField(max_length=255)  # 不可点击
    #
    gl_title = models.CharField(max_length=255)  # 关联标题
    gl_url = models.CharField(max_length=255)  # 关联url