'''
Created on 2017/01/11

@author: akaneko3
'''
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<city_id>\d+)$', views.show, name='show'),
]
