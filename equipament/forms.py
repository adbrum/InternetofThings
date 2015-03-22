#-*- coding: ut-8 -*-
"""
Nome Autor: Adriano Leal
nº Aluno: 11951
911911951@alunos.ipbeja.pt
"""
import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class AddEquipamentForm(forms.Form):

    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True,
                                max_length=30)), label=_("Username"),
                                error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True,
                                max_length=30)),
                                label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True,
                                max_length=30,
                                render_value=False)),
                                label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True,
                                max_length=30,
                                render_value=False)),
                                label=_("Password (again)"))


