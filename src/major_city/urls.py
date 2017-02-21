'''
Created on 2017/01/11

@author: akaneko3
'''
from django.conf.urls import url
from django.views.generic import ListView, DetailView
from .models import City

app_name = 'major_city'
urlpatterns = [
    url(
        r'^$',
        ListView.as_view(
            queryset=City.objects.select_related().all(),
            context_object_name='cities',
            template_name='major_city/list.djhtml'
        ),
        name='index'
    ),
    url(
        r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=City,
            context_object_name='city',
            template_name='major_city/detail.djhtml'
        ),
        name='show'
    ),
]
