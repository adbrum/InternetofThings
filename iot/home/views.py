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
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import json

from iot.models import Equipment, Sensor, RelativePosition


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
    print "equipamentosXXXXXXXXXXXXXXXXXXXXXXXXXXXX" 
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


def getTemplate(request):
    id = request.POST["id"]
    try:
        response_data = RelativePosition.objects.get(id = id).templateJson
    except TemplatesDac.DoesNotExist:
        print "a criar template"
        jsonData = '{"local":{"y":27,"x":41},"temperatura":{"y":73,"x":86},"tempo":{"y":11,"x":174},"publicidade":{"y":209,"x":209},"visitado":{"y":444,"x":95},"competicao":{"y":444,"x":339},"visitante":{"y":444,"x":479},"data":{"y":705,"x":210},"hora":{"y":677,"x":208}}'
        firstTemplate = TemplatesDac(id = 1,
                      descricao = "default",
                      templateJson = jsonData,
                      dataHoraCriacao = dateTime_actual(),
                      utilizadorCriacao = request.user,
                      ativo = True,
                      apagado = False
                )
        firstTemplate.save()
        return redirect('/gestacess/templateDac')
    print response_data, "<---------"
    return HttpResponse(response_data, content_type = "application/json")

@csrf_exempt
def addTemplate(request):
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
    #===========================================================================
    # listaInfo = selectDB(request)
    # if request.method == 'POST':
    #     form = AddFormTemplateDac(request.POST)
    #     if form.is_valid():
    #         newTemplate = TemplatesDac(
    #             descricao = form.cleaned_data['descricao'],
    #             code = form.cleaned_data['code'],
    #             templateJson = form.cleaned_data['templateJson'],
    #             dataHoraCriacao = dateTime_actual(),
    #             utilizadorCriacao = request.user,
    #             ativo = form.cleaned_data['ativo'],
    #             apagado = False
    #             )
    #         newTemplate.save()
    #         # updateInterface(form.cleaned_data['templateJson'])
    #         
    #         if 'SaveAndNew' in request.POST:
    #             return redirect('addTemplateDac')
    #         else:
    #             return redirect('listaTemplates')
    #     else:
    #         print "form nao é valida"
    #         print request.POST
    #         jsonData = request.POST["templateJson"]
    #         template = "gestacess/templateDac/defineTemplate.html"
    # else:
    #     jsonData = """{"local":{"y":27,"x":41},"publicidade":{"y":69,"x":209},"visitado":{"y":444,"x":95},"competicao":{"y":444,"x":339},"visitante":{"y":444,"x":479},"data":{"y":705,"x":210},"hora":{"y":677,"x":208}}"""
    #     form = AddFormTemplateDac()
    #     template = "gestacess/templateDac/defineTemplate.html"
    # eventos = Evento.objects.filter(ativo = 1, apagado = 0)
    # return render_to_response(template,
    #         locals(),
    #         context_instance = RequestContext(request),
    #         )
    #===========================================================================


