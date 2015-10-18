from django.conf.urls import patterns, include, url
from project_1 import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xiangqin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^wechat/$', views.index, name='index'),
    #url(r'^create_menu/$', views.create_menu, name='create_menu'),
    url(r'^test/$', views.test, name='test'),
    url(r'^test2/$', views.test2, name='test2'),
    url(r'^test3/$', views.test3, name='test3'),
    url(r'^reqinfo/$', views.requestInfo, name='reqinfo'),
    url(r'^resinfo/$', views.resInfo, name='resinfo'),
    url(r'^user_info/$', views.user_info, name = 'user_info'),
    url(r'^qrcode/$', views.qrcode, name = 'qrcode'),
    url(r'^detail/(?P<detail_slug>[\w\-]+)/$',views.detail,name='detail'),
)