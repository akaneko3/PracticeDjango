'''
Created on 2017/01/04

@author: akaneko3
'''

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<my_name>\w+)$', views.index),
]
