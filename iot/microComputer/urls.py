# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email l911911951@alunos.ipbeja.pt
"""
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^listMicroComputer/$', 'iot.microComputer.views.listMicroComputer',
                           name="listMicroComputer"),

                       url(r'^addMicroComputer/$', 'iot.microComputer.views.addMicroComputer',
                           name="addMicroComputer"),
                       )
