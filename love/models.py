# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tag(models.Model):
    """
    标签
    """
    name = models.FileField('姓名', upload_to=TGlobalData.STATIC_RECV_PATH, default="", blank=True)  # 图片
    zf = models.CharField('祝福', max_length=128, default="", blank=True)  # 标题
    desc = models.CharField('说明', max_length=256, default="", blank=True)  # 说明
    bak_data = models.CharField('备用字段', max_length=1024, default="", blank=True)  # 备用字段

    def __unicode__(self):
        return str(self.id) + "." + self.title