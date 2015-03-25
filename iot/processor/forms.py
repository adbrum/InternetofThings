# -*- coding: ut-8 -*-
"""
Nome Autor: Adriano Leal
nº Aluno: 11951
911911951@alunos.ipbeja.pt
"""
import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class AddEquipmentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True,
                                                             max_length=100,
                                                             render_value=False)),
                           label=_("Nome"))

    model = forms.CharField(widget=forms.TextInput(attrs=dict(required=True,
                                                              max_length=100,
                                                              render_value=False)),
                            label=_("Modelo"))



