from django.conf.urls import patterns, url
from views import logout_page, register, register_success, home


urlpatterns = patterns('',

    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),

    #url(r'^$', 'django.contrib.auth.views.login'),

    # url(r'^register/$', \
    #     'iot.login.views.register', \
    #     name = "register"),
    #
    # url(r'^logout/$', \
    #     'iot.login.views.logout_page', \
    #     name = "logout"),
    #
    # url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    #
    # url(r'^register/success/$', \
    #     'iot.login.views.register_success', \
    #     name = "success"),
    #
    # url(r'^home/$', \
    #     'iot.login.views.home', \
    #     name = "home"),
)
