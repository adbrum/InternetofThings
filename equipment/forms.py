#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Nome Autor: Adriano Leal
nº Aluno: 11951
911911951@alunos.ipbeja.pt
"""
import re
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _


#Class para editar um tipo documento
class FichaEquipmentForm(ModelForm):

    code = forms.CharField(max_length = 3, label = _(u'Sigla'), widget = forms.TextInput(attrs = {'class':'form-control input-sm pequeno', 'disabled':"disabled"}))
    descricao = forms.CharField(max_length = 30, label = _(u'Descrição'), widget = forms.TextInput(attrs = {'class':'form-control input-sm medio', 'disabled':"disabled"}))


class AddEquipmentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True,
                                                             max_length=100,
                                                             render_value=False)),
                           label=_("Nome"))

    model = forms.CharField(widget=forms.TextInput(attrs=dict(required=True,
                                                              max_length=100,
                                                              render_value=False)),
                            label=_("Modelo"))



