# -*- coding: utf-8 -*-
"""
Nome Autor: Adriano Leal
nº Aluno: 11951
911911951@alunos.ipbeja.pt
"""
from django.contrib import admin
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^', include('login.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
