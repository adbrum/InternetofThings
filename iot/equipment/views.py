# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email: l911911951@alunos.ipbeja.pt
"""

from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_protect
from iot import equipment
from iot.models import Sensor, Equipment


#from forms import AddEquipmentForm, FichaEquipmentForm
#from iot.models import Equipment, PhysicalCharacteristic, Voltage, Memory
def listEquipment_sensor(request, *args, **kwargs):
    
    idTemplate = kwargs['idEquipment']

    TITULO = _(u'Internet das Coisas')
    
    todos_equip = False

    equipamentos = Equipment.objects.filter(id = idTemplate)
    
    for j in equipamentos:
        print'TEMPLATE: ', j.name
    
    
    #===========================================================================
    # response_data = [{"equipamento_id":1, "nomeEquipamento":"EquipSEI_LA", "sensores":[{"sensor_id":2, "nome_sensor":"OLA"}]},
    #  {"equipamento_id":2, "nomeEquipamento":"EquipSEI_LA", "sensores":[{"sensor_id":2, "nome_sensor":"OLA"}]},
    #  {"equipamento_id":3, "nomeEquipamento":"EquipSEI_LA", "sensores":[{"sensor_id":2, "nome_sensor":"OLA"}]}
    #  ]
    #===========================================================================
    
    
    response_data = []
    
    for equipamento in equipamentos:
        
        dictEquip =  {"equipamento_id":equipamento.id,
                      "nomeEquipamento":equipamento.name}
        lSensor = []
        for sensor in equipamento.sensor.all():
            s = Sensor.objects.get(id=sensor.id)
            dictSensor =  {"sensor_id":s.id,
                           "nome_sensor":s.name}
            lSensor.append(dictSensor)
            print s.name
            
        dictEquip["sensores"] = lSensor
        response_data.append(dictEquip)
        
    
    template = "equipment/index.html"
    return render_to_response(template,
                              locals(),
                              context_instance=RequestContext(request)
                              )
    #print json.dumps(response_data)
    
