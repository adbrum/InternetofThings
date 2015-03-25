
# -*- coding: utf-8 -*-
"""
Nome Autor: Adriano Leal
nº Aluno: 11951
911911951@alunos.ipbeja.pt
"""

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_protect

from forms import AddEquipmentForm
from iot.models import Equipment


def listEquipment(request):
    """
    """
    TITULO = _(u'Equipamentos')

    equipamentos = Equipment.objects.all()
    tamLista = len(equipamentos)
    template = "equipment/index.html"
    return render_to_response(template,
                              locals(),
                              context_instance=RequestContext(request)
                              )


@csrf_protect
def addEquipment(request):
    TITULO = _(u'Equipamentos')
    NOME_BREAD = _(u'Novo')
    TITULO_BOTAO = _(u'Guardar')

    saveNew = True

    if request.method == 'POST':
        form = AddEquipmentForm(request.POST)

        # Caso Click em cancelar
        # Retorna para a listagem
        if 'Cancelar' in request.POST or 'listEquipment' in request.POST:
            return HttpResponseRedirect(reverse('listEquipment'))

        if form.is_valid():



            tableEquipament = Equipment(
                name=form.cleaned_data['name'],
                model=form.cleaned_data['model'],
                dataHoraCriacao=datetime.datetime.now(),
                utilizadorCriacao=request.user,
                dataHoraAlteracao=datetime.datetime.now(),
                utilizadorAlteracao=request.user,
            )

            tableEquipament.save()

            if 'SaveAndNew' in request.POST:
                form = AddEquipmentForm()
                template = "equipment/add.html"

            else:
                return HttpResponseRedirect(reverse('listEquipment'))

        else:
            template = "equipment/add.html"

    else:
        # img =  "/static/img/placeholder.png"
        form = AddEquipmentForm()
        template = "equipment/add.html"

    return render_to_response(template,
                              locals(),
                              context_instance=RequestContext(request),
                              )

