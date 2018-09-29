# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-27 17:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('get_web_data', '0009_auto_20180907_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('video_review', models.CharField(max_length=255)),
                ('favorites', models.CharField(max_length=255)),
                ('play', models.CharField(max_length=255)),
                ('bak', models.CharField(max_length=1023, verbose_name='\u5907\u6ce8')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='get_web_data.VideoList')),
            ],
        ),
    ]
