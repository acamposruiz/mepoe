# urls.py
from django.conf.urls import patterns, url
from poems.views import PoemCreate, PoemUpdate, PoemDelete, PoemList, \
    PoemDetail, PoemListUser

urlpatterns = patterns('',
                       # ...
                       url(r'poem/list/$',
                           PoemList.as_view(), name='poem_list'),
                       url(r'poem/user/list/$',
                           PoemListUser.as_view(), name='poem_list_user'),
                       url(r'poem/add/$',
                           PoemCreate, name='poem_add'),
                       url(r'poem/(?P<pk>\d+)/$',
                           PoemDetail.as_view(), name='poem_detail'),
                       url(r'poem/(?P<pk>\d+)/update/$',
                           PoemUpdate, name='poem_update'),
                       url(r'poem/(?P<pk>\d+)/delete/$',
                           PoemDelete.as_view(), name='poem_delete'),
                       # url(r'poem/list/$', PoemList.as_view()),
                       )
