"""panthers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('main.urls', namespace="main", app_name="main")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Feed/', include('feed.urls', namespace='feed', app_name='feed')),
    url(r'^Admission/', include('admission.urls', namespace="admission", app_name="admission")),
    url(r'^About/', include('About.urls', namespace="About", app_name="About")),
    url(r'^board/', include('board.urls', namespace="board", app_name="board")),
    url(r'^help/', include('help.urls', namespace="help", app_name="help")),
    url(r'^ChatRoom/', include('ChatRoom.urls', namespace="ChatRoom", app_name="ChatRoom")),
    url(r'^black_panthers/', include('black_panthers.urls', namespace="black_panthers", app_name="black_panthers")),
]
