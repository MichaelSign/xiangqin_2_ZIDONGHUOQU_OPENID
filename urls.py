#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xiangqin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^wechat/$', 'project_1.views.index'),
    url(r'^create_menu/$','project_1.views.create_menu'),
    url(r'^project_1/', include('project_1.urls')),
)
