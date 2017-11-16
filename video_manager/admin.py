# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
#
from video_manager.models import *

admin.site.register(Tag)
admin.site.register(TestPeople)
admin.site.register(TestVideo)
# admin.site.register(Test_People)
# admin.site.register(Test_Video)

