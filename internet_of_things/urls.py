# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email l911911951@alunos.ipbeja.pt
"""
from django.contrib import admin
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^', include('iot.login.urls')),
                       url(r'^equipments/', include('iot.equipment.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
