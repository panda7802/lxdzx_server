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

from love.views import *
from lxdzx_server import settings
from trans.views import *
from video_manager.views import *
from django.views.static import serve

urlpatterns = [
    url(r'^$', t_index),
    url(r'^MP_verify_e3MyIfTydXwqxprn.txt', t_wx_web),
    url(r'^MP_verify_rhm9oyjPc3nd0dVB.txt', t_wx_web_self),
    url(r'^t_test_amaze/', t_test_amaze),
    url(r'^xnjyshare', xnjyshare),
    url(r'^test_layui/(.*)', t_test_layui),
    url(r'^admin/', admin.site.urls),
    url(r'^trans/(.*)', trans_url),
    url(r'^notice/', notice),
    url(r'^wx_token/', wx_token),
    url(r'^login', login),
    # url(r'^lxdzx/', t_index),
    url(r'^lxdzx/(.*)', lxdzx),
    url(r'^lxdzx_show/(.*)', lxdzx_show),
    url(r'^static/(?P<path>.*)$', serve, {'document_root', settings.STATIC_ROOT,}),
    url(r'^love/', love_index),
]
