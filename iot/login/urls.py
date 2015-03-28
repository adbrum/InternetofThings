# -*- coding: utf-8 -*-
"""
Nome Autor: Adriano Leal
nÂº Aluno: 11951
911911951@alunos.ipbeja.pt
"""
from django.conf.urls import patterns, url
from views import logout_page, register, register_success, home


urlpatterns = patterns('',

                       url(r'^$', 'django.contrib.auth.views.login'),

)
