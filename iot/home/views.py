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
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import json

from iot.models import Equipment, Sensor


@login_required
def index(request):
    """
    Página principal do utilizador
    """

    TITULO = _(u'Internet das Coisas')

 #==============================================================================
 #    equipamentos = Equipment.objects.all()
 #     
 #    retorno = serializers.serialize("json",  equipamentos)
 #     
 #    for i in equipamentos:
 #         
 #        for z in i.sensor.all():
 #            print z
 # 
 #     
 #     
 #    tamLista = len(equipamentos)
 #==============================================================================
    
    template = "home/index.html"
    return render_to_response(template,
                              locals(),
                              context_instance=RequestContext(request)
                              )

#@login_required
@csrf_exempt
def equipamentos(request):
    print "equipamentos"
    """
    Página principal do utilizador
    """

    TITULO = _(u'Internet das Coisas')

    equipamentos = Equipment.objects.all()
    
    
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
            '''
            response_data.append(
                           {"equipamento_id":equipamento.id,
                             "nomeEquipamento":equipamento.name,
                             "sensores":[{"sensor_id":s.id,
                                          "nome_sensor":s.name}]
                            })
            '''
            
        dictEquip["sensores"] = lSensor
        response_data.append(dictEquip)
        
        
    print json.dumps(response_data)
#===============================================================================
#     
#     retorno1 = {}    
#     for i in equipamentos:
#         
#         for sensor in i.sensor.all():
#             print sensor
#             retorno1 = {i:{sensor}} 
#             
#             
#     retorno = serializers.serialize("json",  equipamentos)
#     retornof = serializers.serialize("json",  retorno1)
# 
#     tamLista = len(equipamentos)
#     
#     response = {"retorno":retorno, "retorno1":retornof}
#===============================================================================
    
    #return HttpResponse(retorno, mimetype="text/javascript")
    return HttpResponse(json.dumps(response_data), content_type = "application/json")






