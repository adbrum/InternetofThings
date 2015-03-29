# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email l911911951@alunos.ipbeja.pt
"""
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^listEquipment/$', 'iot.equipment.views.listEquipment',
                           name="listEquipment"),

                       url(r'^addEquipment/$', 'iot.equipment.views.addEquipment',
                           name="addEquipment"),
                       )
