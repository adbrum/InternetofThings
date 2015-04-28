# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email l911911951@alunos.ipbeja.pt
"""
from django.conf.urls import patterns, url
from iot import *


urlpatterns = patterns('',
                       url(r'^$', 'iot.home.views.index', name="home"),
                       url(r'^equipamentos', 'iot.home.views.equipamentos', name="equipamentos"),
                       url(r'^getTemplate', 'iot.home.views.getTemplate', name="getTemplate"),
                       url(r'^addTemplate', 'iot.home.views.addTemplate', name="addTemplate"),
                       )

