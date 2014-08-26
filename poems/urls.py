# urls.py
from django.conf.urls import patterns, url
from poems.views import PoemCreate, PoemUpdate, PoemDelete, PoemList, PoemDetail

urlpatterns = patterns('',
                       # ...
                       url(r'poem/list', PoemList.as_view(),
                           name='poem_list'),
                       url(r'poem/add/$', PoemCreate.as_view(),
                           name='poem_add'),
                       url(r'poem/(?P<pk>\d+)/$',
                           PoemDetail.as_view(), name='poem_view'),
                       url(r'poem/(?P<pk>\d+)/update/$',
                           PoemUpdate.as_view(), name='poem_update'),
                       url(r'poem/(?P<pk>\d+)/delete/$',
                           PoemDelete.as_view(), name='poem_delete'),
                       url(r'poem/list/$', PoemList.as_view()),
                       )
