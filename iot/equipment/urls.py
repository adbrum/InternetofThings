# -*- coding: utf-8 -*-
"""
Nome Autor: Adriano Leal
nº Aluno: 11951
911911951@alunos.ipbeja.pt
"""
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^listEquipment/$', 'iot.equipment.views.listEquipment',
                           name="listEquipment"),

                       url(r'^addEquipment/$', 'iot.equipment.views.addEquipment',
                           name="addEquipment"),
                       )
