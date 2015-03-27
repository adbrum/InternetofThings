# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email l911911951@alunos.ipbeja.pt
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
                       url(r'^', include('iot.login.urls')),
                       url(r'^equipments/', include('iot.equipment.urls')),
                       url(r'^processors/', include('iot.processor.urls')),
                       url(r'^microComputers/', include('iot.microComputer.urls')),
                       url(r'^sensors/', include('iot.sensor.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
