from django.contrib import admin
from django.urls import path
from public import views
from django.conf.urls import url

urlpatterns = [
    url(r'site', views.site, name='index'),
]
