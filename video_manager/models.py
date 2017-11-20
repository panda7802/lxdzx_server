# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.db import models

# Create your models here.
from django.utils import timezone

from tutils.t_global_data import TGlobalData


# class TestPeople(models.Model):
#     name = models.CharField(max_length=150)
#     age = models.IntegerField()
#     desc = models.CharField(max_length=512)
#
#     def __str__(self):
#         return self.name
#
#
# class TestVideo(models.Model):
#     name = models.CharField(max_length=150)
#     pic_url = models.CharField(max_length=512)
#     video_url = models.CharField(max_length=512)
#
#     def __str__(self):
#         return self.name


class Tag(models.Model):
    """
    标签
    """
    pic_url = models.FileField('图片', upload_to=TGlobalData.STATIC_RECV_PATH, default="", blank=True)  # 图片
    title = models.CharField('标题', max_length=128, default="", blank=True)  # 标题
    desc = models.CharField('说明', max_length=256, default="", blank=True)  # 说明
    bak_data = models.CharField('备用字段', max_length=1024, default="", blank=True)  # 备用字段

    def __unicode__(self):
        return self.title


class Video(models.Model):
    """
    视频内容
    """
    title = models.CharField('标题', max_length=128, default="", blank=True)  # 标题
    pic_url = models.FileField('图片', upload_to=TGlobalData.STATIC_RECV_PATH, default="", blank=True)  # 图片
    video_url = models.CharField('视频地址', max_length=1024, default="", blank=True)  # 视频地址
    desc = models.CharField('描述', max_length=1024, default="", blank=True)  # 描述
    tags = models.ManyToManyField(Tag)  # 标签
    upload_time = models.DateTimeField('保存日期', default=timezone.now)  # 时间
    recommend = models.IntegerField('推荐', default=0)  # 推荐，分越高，越推荐
    keywords = models.CharField('关键字(用英文状态下逗号分隔)', max_length=1024, default="", blank=True)  # 关键字
    bak_data = models.CharField('备用字段', max_length=1024, default="", blank=True)  # 备用字段

    def __unicode__(self):
        return self.title


class People(models.Model):
    """
    人员信息
    """
    SEX_CHOICES = (
        (0, '未录入'),
        (1, '男'),
        (2, '女'),
    )
    name = models.CharField('标题', max_length=64, default="", blank=True)  # 标题
    pwd = models.CharField('密码', max_length=64, default="", blank=True)  # 密码
    sex = models.IntegerField('性别', choices=SEX_CHOICES, default=0)
    phone = models.CharField('手机号', max_length=64, default="", blank=True)  # 手机号
    wx_name = models.CharField('微信名称', max_length=128, default="", blank=True)  # 微信名称
    bak_data = models.CharField('备用字段', max_length=1024, default="", blank=True)  # 备用字段

    def __unicode__(self):
        return self.name


class Video_Record(models.Model):
    """
    播放记录
    """
    video_id = models.ForeignKey(Video)
    people_id = models.ForeignKey(People)
    watch_time = models.DateTimeField('观看时间', default=timezone.now)  # 时间
    bak_data = models.CharField('备用字段', max_length=1024, default="", blank=True)  # 备用字段

    def __unicode__(self):
        try:
            s = self.watch_time, "-", People.objects.filter(id=self.video_id)[0]
        except Exception, e:
            logging.error(str(e))
            s = "get db err"
        return s


class Video_Score(models.Model):
    """
    评分
    """
    video_id = models.ForeignKey(Video)
    people_id = models.ForeignKey(People)
    score = models.FloatField('评分', default=-1)  # 评分
    comment = models.CharField('评论', max_length=1024, default="", blank=True)
    bak_data = models.CharField('备用字段', max_length=1024, default="", blank=True)  # 备用字段

    def __unicode__(self):
        try:
            s = People.objects.filter(id=self.video_id)[0]
        except Exception, e:
            logging.error(str(e))
            s = "get db err"
        return s
