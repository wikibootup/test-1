from django.conf.urls import patterns, include, url
from django.contrib import admin
from test_project.views import Home 

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', Home.as_view(), name='home'),
)
