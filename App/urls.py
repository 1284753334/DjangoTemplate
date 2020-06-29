from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from App import views

urlpatterns = [
    url(r'^hello/',views.hello ),
    url(r'^index', views.index),
    url(r'^getstudents', views.get_students),
    url(r'^tem', views.temp),
    url(r'^home', views.home),
]