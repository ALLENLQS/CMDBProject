#! /usr/bin/env python3
# -*- coding : utf-8 -*-
# Author     : ALLEN
# @Time      : 2018/11/13 0013 上午 10:33

from django.conf.urls import include,url
from User.views import *
urlpatterns = [
    url(r'^register/',register),
]