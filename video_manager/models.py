# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class TestPeople(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    desc = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class TestVideo(models.Model):
    name = models.CharField(max_length=150)
    pic_url = models.CharField(max_length=512)
    video_url = models.CharField(max_length=512)

    def __str__(self):
        return self.name


