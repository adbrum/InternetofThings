#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Nome Autor: Adriano Leal
nº Aluno: 11951
911911951@alunos.ipbeja.pt
"""
from django import forms
from django.utils.translation import ugettext_lazy as _
#Class para editar um tipo documento
from iot.models import Equipment


class FichaEquipmentForm(forms.Form):

    name = forms.CharField(max_length = 50, 
                           label = _(u'Nome'), 
                           widget = forms.TextInput(attrs = {'class':'form-control input-sm m', 'disabled':"disabled"}))
    
    model = forms.CharField(max_length = 50,
                             label = _(u'Modelo'),
                              widget = forms.TextInput(attrs = {'class':'form-control input-sm medio', 'disabled':"disabled"}))


class AddEquipmentForm(forms.Form):
    
    name = forms.CharField(max_length = 50, \
                           label = _(u'Nome'), \
                           widget = forms.TextInput(attrs = {'class':'form-control input-sm pequeno required_form', 'autofocus':"autofocus"}))
    
    model = forms.CharField(max_length = 30, \
                                label = _(u'Modelo'), \
                                widget = forms.TextInput(attrs = {'class':'form-control input-sm medio required_form'}))
    


    class Meta:
        model = Equipment 
        fields = []
