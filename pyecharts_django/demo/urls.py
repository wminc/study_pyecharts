# -*- coding:utf8 -*-
"""
Created on 2019/9/26 17:18

@author: minc
"""

from django.conf.urls import url

from . import views

app_name = 'demo'
urlpatterns = [
    url(r'^test_demo/$', views.test_demo, name='test_demo'),

    url(r'^show_demo01/$', views.show_demo01, name='show_demo01'),

    url(r'^index02/$', views.index02, name='index02'),
    url(r'^show_demo02/$', views.show_demo02, name='show_demo02'),

    url(r'^index03/$', views.index03, name='index03'),
    url(r'^show_demo03/$', views.show_demo03, name='show_demo03'),
    url(r'^demo03DynamicData/$', views.demo03DynamicData, name='demo03DynamicData')
]
