from django.conf.urls import patterns, include, url
from .views import *
from django.conf import settings
from haystack.views import SearchView
try:
    SearchView.func_globals = SearchView.func_globals
except:
    SearchView.func_globals = {}

# from settings.settings import MEDIA_ROOT

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', home, name="home"),
                       url(r'^accounts/', include('allauth.urls')),
                       url(r'^avatar/', include('avatar.urls')),
                       url(r'^', include('favorite.urls')),
                       # url(r'^accounts/', include('userena.urls')),
                       url(r'^accounts/', include(
                           'userprofiles.urls', namespace="userprofiles")),
                       url(r'^', include(
                           'poems.urls', namespace="poems")),
                       url(r'^search/', include('haystack.urls')),
                       )

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$',
                                'django.views.static.serve', {
                                'document_root':
                                settings.MEDIA_ROOT,
                                'show_indexes': True}),

                            )
