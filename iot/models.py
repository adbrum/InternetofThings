# -*- coding: utf-8 -*-
"""
Nome Autor: Adriano Leal
nº Aluno: 11951
911911951@alunos.ipbeja.pt
"""
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class MicroComputer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    model = models.CharField(max_length=100, verbose_name='Modelo')
    processor = models.ForeignKey('Processor', verbose_name='Processador')
    GPU = models.ForeignKey('GPU')
    operatingSystems = models.ForeignKey('OperatingSystem', verbose_name='Sistema Operativo')
    dateManufacture = models.DateField(verbose_name='Data de Fabrico')
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    userCreation = models.CharField(max_length=100, verbose_name='Criado por')
    dateTimeChange = models.DateTimeField(auto_now=True)
    userAmendment = models.CharField(max_length=100, verbose_name='Alterado por')
    
    class Meta:
        verbose_name = 'Micro Computador'
        verbose_name_plural = 'Micros Computadores'

    def __unicode__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    model = models.CharField(max_length=100, verbose_name='Modelo')
    microComputer = models.ForeignKey('microComputer', verbose_name='Micro Computador')
    sensor = models.ForeignKey('Sensor', verbose_name='Sensor')
    expansion = models.ForeignKey('Expansion', verbose_name='Expensão')
    accessory = models.ForeignKey('Accessory', verbose_name='Acessório')
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    userCreation = models.CharField(max_length=100, verbose_name='Criado por')
    dateTimeChange = models.DateTimeField(auto_now=True)
    userAmendment = models.CharField(max_length=100, verbose_name='Alterado por')
    
    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'

    def __unicode__(self):
        return self.name

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Sensor'
        verbose_name_plural = 'Sensores'



class PhysicalCharacteristic(models.Model):
    microComputer = models.ForeignKey('microComputer', verbose_name='Micro Computador')
    length = models.FloatField(verbose_name='Comprimento')
    width = models.FloatField(verbose_name='Largura')
    weight = models.IntegerField(verbose_name='Peso')
    
    class Meta:
        verbose_name = 'Característica Física'
        verbose_name_plural = 'Características Físicas'


class Voltage(models.Model):
    microComputer = models.ForeignKey('microComputer', verbose_name='Micro Computador')
    operatingVoltage = models.IntegerField(verbose_name='Voltagem Operacional')
    IOCurrentMax = models.IntegerField(verbose_name='I/O Corrente máxima')
    inputVoltageRecommended = models.IntegerField(verbose_name='Voltagem recomendada')
    DCCurrentperIOPin = models.IntegerField(blank=True, verbose_name='DC Corrente por pino')
    DCCurrentfor3_3VPin = models.IntegerField(blank=True, verbose_name='DC Corrente por 3.3 pino')
    powerRatings = models.CharField(blank=True, max_length=50, verbose_name='Classificações de energia')
    powerSource = models.CharField(blank=True, max_length=50, verbose_name='Fonte de energia')
    
    class Meta:
        verbose_name = 'Voltagem'
        verbose_name_plural = 'Voltagens'


class GPU(models.Model):
    type = models.CharField(max_length=100, verbose_name='Tipo')
    clockSpeed = models.IntegerField(verbose_name='Clock Speed')
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    userCreation = models.CharField(max_length=100, verbose_name='Criado por')
    dateTimeChange = models.DateTimeField(auto_now=True)
    userAmendment = models.CharField(max_length=100, verbose_name='Alterado por')
    
    class Meta:
        verbose_name = 'GPU'
        verbose_name_plural = 'GPUs'


class Processor(models.Model):
    type = models.CharField(max_length=100, verbose_name='Processador')
    clockSpeed = models.IntegerField(verbose_name='Clock Speed')
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    userCreation = models.CharField(max_length=100, verbose_name='Criado por')
    dateTimeChange = models.DateTimeField(auto_now=True)
    userAmendment = models.CharField(max_length=100, verbose_name='Alterado por')
    
    def __unicode__(self):
        return self.type
    
    class Meta:
        verbose_name = 'Processador'
        verbose_name_plural = 'Processadores'


class Interface(models.Model):
    microComputer = models.ForeignKey('microComputer', verbose_name='Micro Computador')
    hdmi = models.CharField(blank=True, max_length=50)
    USBPorts = models.CharField(blank=True, max_length=50, verbose_name='Porta USB')
    videoInput = models.CharField(blank=True, max_length=50, verbose_name='Entrada de vídeo')
    videoOutputs = models.CharField(blank=True, max_length=50, verbose_name='Saida de vídeo')
    audioInputs = models.CharField(blank=True, max_length=50, verbose_name='Entrada de audio')
    audioOutputs = models.CharField(blank=True, max_length=50, verbose_name='Saida de audio')
    storage = models.CharField(blank=True, max_length=50, verbose_name='Armazenamento')
    network = models.CharField(blank=True, max_length=50, verbose_name='Rede')
    jack = models.CharField(blank=True, max_length=50)
    digitalIOPins = models.IntegerField(blank=True, verbose_name='Pinos I/O digital')
    analogInputPins = models.IntegerField(blank=True, verbose_name='Pinos de entrada analógica')
    
    class Meta:
        verbose_name = 'Interface'
        verbose_name_plural = 'Interfaces'


class OperatingSystem(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    version = models.CharField(max_length=50, verbose_name='Versão')
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    userCreation = models.CharField(max_length=100, verbose_name='Criado por')
    dateTimeChange = models.DateTimeField(auto_now=True)
    userAmendment = models.CharField(max_length=100, verbose_name='Alterado por')
    
    class Meta:
        verbose_name = 'Sistema Operativo'
        verbose_name_plural = 'Sistemas Operativos'


class Expansion(models.Model):
    type = models.CharField(max_length=100, verbose_name='Tipo')
    peripherals = models.CharField(max_length=50, verbose_name='Periféricos')
    GPIO = models.IntegerField()
    
    class Meta:
        verbose_name = 'Expansão'
        verbose_name_plural = 'Expansões'


class Accessory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    type = models.CharField(max_length=100, verbose_name='Tipo')
    
    class Meta:
        verbose_name = 'Acessório'
        verbose_name_plural = 'Acessórios'


class Memory(models.Model):
    microComputer = models.ForeignKey('microComputer', verbose_name='Micro Computador')
    RAM = models.IntegerField(blank=True)
    SRAM = models.IntegerField(blank=True)
    EEPROM = models.IntegerField(blank=True)
    flashMemory = models.IntegerField(blank=True, verbose_name='Memória Flash')
    
    class Meta:
        verbose_name = 'Memória'
        verbose_name_plural = 'Memórias'

