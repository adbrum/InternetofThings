# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email l911911951@alunos.ipbeja.pt
"""

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_protect

from iot.models import Equipment, Sensor


@login_required
def index(request):
    """
    Página principal do utilizador
    """

    TITULO = _(u'Internet das Coisas')

    equipamentos = Equipment.objects.all()
    
    retorno = serializers.serialize("json",  equipamentos)
    
    for i in equipamentos:
        
        for z in i.sensor.all():
            print z

    
    
    tamLista = len(equipamentos)
    
    template = "home/index.html"
    return render_to_response(template,
                              locals(),
                              context_instance=RequestContext(request)
                              )

