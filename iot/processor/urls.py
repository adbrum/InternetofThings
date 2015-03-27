# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email l911911951@alunos.ipbeja.pt
"""
from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^listProcessors/$', 'iot.processor.views.listProcessor',
                           name="listProcessors"),

                        url(r'^addProcessor/$', 'iot.processor.views.addProcessor',
                            name="addProcessor"),
                       )
