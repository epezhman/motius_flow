"""motius_flow URL Configuration

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
from main import views
from django.contrib.auth import views as auth_views
from user import urls as user_urls
from question_board import urls as question_urls

urlpatterns = [
    url(r'^$', views.home, name="motiusflow_home"),
    url(r'^user/', include(user_urls)),
    url(r'^question_board/', include(question_urls)),
    url(r'^admin/', include(admin.site.urls)),
]


urlpatterns += [
    url(r'^login/$', auth_views.login,
        {'template_name': 'login.html'}, name="motiusflow_login"),
    url(r'^logout/$', auth_views.logout,
        {'next_page': 'motiusflow_home'}, name="motiusflow_logout"),
]