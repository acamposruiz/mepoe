# urls.py
from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
    url(r'signup/$', signup, name='signup'),
    url(r'signin/$', signin, name='signin'),
)