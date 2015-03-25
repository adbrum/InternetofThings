# -*- coding: utf-8 -*-
"""
Nome Autor: Adriano Leal
nº Aluno: 11951
911911951@alunos.ipbeja.pt
"""
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^listProcessors/$',
                           'InternetofThings.equipment.views.listProcessors',
                           name="listProcessors"),

                       url(r'^addProcessor/$',
                           'InternetofThings.equipment.views.addProcessor',
                           name="addProcessor"),
                       )
