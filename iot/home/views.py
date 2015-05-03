# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email l911911951@alunos.ipbeja.pt
"""

import json

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from iot.models import Equipment, Sensor, RelativePosition, Template


@login_required(login_url='/admin/login/')
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
# Dac
#     tamLista = len(equipamentos)
#     
#     response = {"retorno":retorno, "retorno1":retornof}
#===============================================================================
    
    #return HttpResponse(retorno, mimetype="text/javascript")
    return HttpResponse(json.dumps(response_data), content_type = "application/json")

@csrf_exempt
def getEquipmentPosition(request):
    print'TEMPLATEXXXXXXXXXXXXXXXXXXXXXXXXXXXxx'
    posicao = RelativePosition.objects.all()
   
    response_data = []
    
    for item in posicao:
        print'POSICAO VIEW ', item.nameElement
        
        #dictEquip =                                
                              
        response_data.append({"nome":item.nameElement,
                              "X":item.leftX,
                              "Y":item.topY})
    
    
    return HttpResponse(json.dumps(response_data), content_type = "application/json")

@csrf_exempt
def addEquipmentPosition(request):
    #print'RQUEST XXXXXXXXXXXXXXXXXXXXXXXXX',request.POST
    
    #Recebe a string pelo POST e a transforma em objeto.
    dados = json.loads(request.POST.get('dados'))
    print "AQUI", dados
    for equipamento, valores in dados.iteritems():
        print "EQUIPAMENTO ", equipamento, "VALORES", valores
        dict = {"topY": valores["y"], "leftX":valores["x"]}
          
        posicaoTable = RelativePosition.objects.update_or_create(nameElement = equipamento,
                                        defaults=dict
                                        )
    
    return HttpResponse(content_type = "application/json")

@csrf_exempt
def getTemplate(request):
    template = Template.objects.all()
   
    response_data = []
    
    for item in template:
        print'CAMINHO: ', item.name
        
        #dictEquip =                                
                              
        response_data.append({"nome":item.name,
                              "caminhoImagem":item.imagePath})
    
    
    return HttpResponse(json.dumps(response_data), content_type = "application/json")


