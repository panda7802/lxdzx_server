# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_manager', '0002_people_tag_video_video_record_video_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='pic_url',
            field=models.FileField(blank=True, default='', upload_to=b'E:\\pythonCode\\lxdzx_server/static/files/recv', verbose_name='\u56fe\u7247'),
        ),
    ]
