# -*- coding: utf-8 -*-
"""
Nome Autor: Adriano Leal
nº Aluno: 11951
911911951@alunos.ipbeja.pt
"""

from django.core.urlresolvers import reverse
from django.utils.datetime_safe import datetime
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.utils.translation import ugettext, ugettext_lazy as _
from InternetofThings.internet_of_things.models import Equipment

from forms import *


def listEquipament(request):
    """
    """
    TITULO = _(u'Equipamentos')

    equipament = Equipment.objects.all()
    tamLista = len(equipament)
    template = "equipament/index.html"

    return render_to_response(template,
         locals(),
         context_instance = RequestContext(request)
         )


@csrf_protect
def addEquipament(request):

    TITULO = _(u'Equipamentos')
    NOME_BREAD = _(u'Novo')
    TITULO_BOTAO = _(u'Guardar')

    saveNew = True

    if request.method == 'POST':
        form = AddEquipamentForm(request.POST)

        # Caso Click em cancelar
        # Retorna para a listagem
        if 'Cancelar' in request.POST  or 'listEquipament' in request.POST:
            return HttpResponseRedirect(reverse('listEquipament'))

        if form.is_valid():


            tableEquipament = Equipment(
                        dataHoraCriacao = datetime.datetime.now(),
                        utilizadorCriacao = request.user,
                        dataHoraAlteracao = datetime.datetime.now(),
                        utilizadorAlteracao = request.user,
                        )


            tableEquipament.save()


            if 'SaveAndNew' in request.POST:
                form = AddEquipamentForm()
                template = "equipament/add.html"

            else:
                return HttpResponseRedirect(reverse('listEquipament'))

        else:
            template = "gestvisitor/config/tipos_doc/addTipoDoc.html"

    else:
        #img =  "/static/img/placeholder.png"
        form = AddEquipamentForm()
        template = "equipament/add.html"


    return render_to_response(template,
        locals(),
        context_instance = RequestContext(request),
        )

