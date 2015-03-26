# -*- coding: utf-8 -*-
"""
:Autor Adriano Leal
:Aluno 11951
:email l911911951@alunos.ipbeja.pt
"""
from django import forms
from django.utils.translation import ugettext_lazy as _
# Class para editar um tipo documento
from iot.models import Equipment


class FichaPeocessorForm(forms.Form):

    type = forms.CharField(max_length=50, \
                                label=_(u'Tipo'), \
                                widget=forms.TextInput(attrs={'class':'form-control input-sm medio required_form', 'disabled':"disabled"}))

    clockSpeed = forms.FloatField(
                                label=_(u'Clock Speed'), \
                                widget=forms.TextInput(attrs={'class':'form-control input-sm medio required_form', 'disabled':"disabled"}))


class AddProcessorForm(forms.Form):
    type = forms.CharField(max_length=50, \
                                label=_(u'Tipo'), \
                                widget=forms.TextInput(attrs={'class':'form-control input-sm medio required_form'}))

    clockSpeed = forms.FloatField(
                                label=_(u'Clock Speed'), \
                                widget=forms.TextInput(attrs={'class':'form-control input-sm medio required_form'}))

