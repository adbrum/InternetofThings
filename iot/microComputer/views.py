# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email l911911951@alunos.ipbeja.pt
"""

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_protect

from forms import AddMicroComputerForm, FichaMicroComputerForm
from iot.models import MicroComputer, PhysicalCharacteristic, Voltage, Memory


def listMicroComputer(request):
    """
    Lista todos os microComputers registrados
    """
    
    TITULO = _(u'Micro Computadores')

    microComputers = MicroComputer.objects.all()
    tamLista = len(microComputers)
    template = "microComputer/index.html"
    return render_to_response(template,
                              locals(),
                              context_instance=RequestContext(request)
                              )


@csrf_protect
def addMicroComputer(request):
    """
    Adiciona um equipamento novo
    """
    
    TITULO = _(u'Micro Computadores')
    NOME_BREAD = _(u'Novo')
    TITULO_BOTAO = _(u'Guardar')

    saveNew = True

    if request.method == 'POST':
        form = AddMicroComputerForm(request.POST)

        # Caso Click em cancelar
        # Retorna para a listagem
        if 'Cancelar' in request.POST or 'listMicroComputer' in request.POST:
            return HttpResponseRedirect(reverse('listMicroComputer'))

        if form.is_valid():

            tableEquipament = MicroComputer(
                name=form.cleaned_data['name'],
                model=form.cleaned_data['model'],
               
                dataHoraCriacao=datetime.datetime.now(),
                utilizadorCriacao=request.user,
                dataHoraAlteracao=datetime.datetime.now(),
                utilizadorAlteracao=request.user,
            )
            
            tableEquipament.save()
           
            microComputer = tableEquipament.id,
            
            tablePhysicalCharac = PhysicalCharacteristic(
                microComputer=microComputer,
                dateManufacture=form.cleaned_data['dateManufacture'],
                length=form.cleaned_data['length'],
                width=form.cleaned_data['width'],
                weight=form.cleaned_data['weight'],
            )
            
            tablePhysicalCharac.save()
            
            
            tableVoltage = Voltage(
                microComputer=microComputer,
                operatingVoltage=form.cleaned_data['operatingVoltage'],
                IOCurrentMax=form.cleaned_data['IOCurrentMax'],
                inputVoltageRecommended=form.cleaned_data['inputVoltageRecommended'],
                DCCurrentperIOPin=form.cleaned_data['DCCurrentperIOPin'],
                DCCurrentfor3_3VPin=form.cleaned_data['DCCurrentfor3_3VPin'],
                powerRatings=form.cleaned_data['powerRatings'],
                powerSource=form.cleaned_data['powerSource'],
            )
                         
            tableVoltage.save()
            
            tableMemory = Memory(
                microComputer=microComputer,
                RAM=form.cleaned_data['RAM'],
                SRAM=form.cleaned_data['SRAM'],
                EEPROM=form.cleaned_data['EEPROM'],
                flashMemory=form.cleaned_data['flashMemory'],
            )
            
            tableMemory.save()

            
            if 'SaveAndNew' in request.POST:
                form = AddMicroComputerForm()
                template = "microComputer/add.html"

            else:
                return HttpResponseRedirect(reverse('listMicroComputer'))

        else:
            template = "microComputer/add.html"

    else:
        # img =  "/static/img/placeholder.png"
        form = AddMicroComputerForm()
        template = "microComputer/add.html"

    return render_to_response(template,
                              locals(),
                              context_instance=RequestContext(request),
                              )

