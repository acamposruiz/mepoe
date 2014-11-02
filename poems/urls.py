# urls.py
from django.conf.urls import patterns, url
from poems.views import *

urlpatterns = patterns('',
                       # ...
                       url(r'poem/list/$',
                           PoemList.as_view(), name='poem_list'),

                       url(r'poem/list/user/(\d+)/$',
                           PoemListUser.as_view(), name='poem_list_user'),

                       url(r'poem/list/author/(\d+)/$',
                           PoemListAuthor.as_view(),
                           name='poem_list_author'),

                       url(r'poem/list/favorites/(\d+)/$',
                           PoemListFavorites.as_view(),
                           name='poem_list_favorites'),

                       url(r'poem/list/book/(\d+)/$',
                           PoemListBook.as_view(), name='poem_list_book'),

                       url(r'poem/list/user/$',
                           PoemListUser.as_view(), name='poem_list_user'),

                       url(r'poem/add/$',
                           PoemCreate, name='poem_add'),

                       url(r'poem/(?P<pk>\d+)/update/$',
                           PoemUpdate, name='poem_update'),

                       url(r'poem/(?P<pk>\d+)/delete/$',
                           PoemDelete.as_view(), name='poem_delete'),

                       url(r'poem/(?P<pk>\d+)/(?P<list>\w*)/$',
                           PoemDetail.as_view(), name='poem_detail'),

                       # url(r'poem/list/$', PoemList.as_view()),
                       )
