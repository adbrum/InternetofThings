# -*- coding: utf-8 -*-
"""
Nome Autor: Adriano Leal
nº Aluno: 11951
911911951@alunos.ipbeja.pt
"""
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^listEquipment/$',
                           'InternetofThings.equipment.views.listEquipment',
                           name="listEquipment"),

                       url(r'^addEquipment/$',
                           'InternetofThings.equipment.views.addEquipment',
                           name="addEquipment"),
                       )
