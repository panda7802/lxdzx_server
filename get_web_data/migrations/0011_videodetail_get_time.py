# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-29 09:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('get_web_data', '0010_videodetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='videodetail',
            name='get_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u4fdd\u5b58\u65e5\u671f'),
        ),
    ]
