# -*- coding: utf-8 -*-
"""
:Autor Adriano Leal
:Aluno 11951
:email l911911951@alunos.ipbeja.pt
"""

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_protect

from forms import FichaPeocessorForm, AddProcessorForm
from iot.models import Equipment, PhysicalCharacteristic, Voltage, Memory


#from iot.processor.forms import AddProcessorForm, FichaPeocessorForm
def listProcessor(request):
    """
    Lista todos os processadors registrados
    """
    
    TITULO = _(u'Processadores')

    processadors = Equipment.objects.all()
    tamLista = len(processadors)
    template = "processor/index.html"
    return render_to_response(template,
                              locals(),
                              context_instance=RequestContext(request)
                              )


@csrf_protect
def addProcessor(request):
    """
    Adiciona um processador novo
    """MicroComputer = models.ForeignKey('MicroComputer')
    
    TITULO = _(u'Processadores')
    NOME_BREAD = _(u'Novo')
    TITULO_BOTAO = _(u'Guardar')

    saveNew = True

    if request.method == 'POST':
        form = AddProcessorForm(request.POST)

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
           
            processor = tableEquipament.id,
            
            tablePhysicalCharac = PhysicalCharacteristic(
                processor=processor,
                dateManufacture=form.cleaned_data['dateManufacture'],
                length=form.cleaned_data['length'],
                width=form.cleaned_data['width'],
                weight=form.cleaned_data['weight'],

            )
            
            tablePhysicalCharac.save()
            
            
            tableVoltage = Voltage(
                processor=processor,
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
                processor=processor,
                RAM=form.cleaned_data['RAM'],
                SRAM=form.cleaned_data['SRAM'],
                EEPROM=form.cleaned_data['EEPROM'],
                flashMemory=form.cleaned_data['flashMemory'],
            )
            
            tableMemory.save()

            
            if 'SaveAndNew' in request.POST:
                form = AddProcessorForm()
                template = "processor/add.html"

            else:
                return HttpResponseRedirect(reverse('listEquipment'))

        else:
            template = "processor/add.html"

    else:
        # img =  "/static/img/placeholder.png"
        form = AddProcessorForm()
        template = "processor/add.html"

    return render_to_response(template,
                              locals(),
                              context_instance=RequestContext(request),
                              )