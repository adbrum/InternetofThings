from django.contrib import admin
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'internet_of_things.views.home', name='home'),
    url(r'^', include('iot.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
