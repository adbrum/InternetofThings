# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email l911911951@alunos.ipbeja.pt
"""
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^listSensor/$', 'iot.sensor.views.listSensor',
                           name="listSensor"),

                       url(r'^addSensor/$', 'iot.sensor.views.addSensor',
                           name="addSensor"),
                       )
