"""lxdzx_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from lxdzx_server import settings
from trans.views import *
from video_manager.views import *
from django.views.static import serve

urlpatterns = [
    url(r'^$', t_index),
    url(r'^admin/', admin.site.urls),
    url(r'^trans/(.*)', trans_url),
    url(r'^login', login),
    url(r'^get_tags', get_tags),
    url(r'^get_video_by_id', get_video_by_id),
    url(r'^get_file/(.*)', get_file),
    url(r'^get_video_by_tag', get_video_by_tag),
    url(r'^get_videos_oder', get_videos_order),
    url(r'^get_video_by_gjz', get_video_by_gjz),
    url(r'^play_video', play_video),
    url(r'^static/(?P<path>.*)$', serve, {'document_root', settings.STATIC_ROOT,}),
]
