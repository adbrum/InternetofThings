# -*- coding: utf-8 -*-
"""
Nome Autor: Adriano Leal
nº Aluno: 11951
911911951@alunos.ipbeja.pt
"""
from datetime import datetime

from audit_log.models.fields import CreatingUserField, LastUserField
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class MicroComputer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    model = models.CharField(max_length=100, verbose_name='Modelo')
    processor = models.ForeignKey('Processor', blank=True, verbose_name='Processador')
    microcontroller = models.ForeignKey('Microcontroller', blank=True, verbose_name='Microcontrolador')
    GPU = models.ForeignKey('GPU', blank=True)
    operatingSystems = models.ForeignKey('OperatingSystem', blank=True, verbose_name='Sistema Operativo')
    dateManufacture = models.DateField(blank=True, verbose_name='Data de Fabrico')
    userCreation = CreatingUserField(related_name="created_microcomputer")
    userAmendment = LastUserField()
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    dateTimeChange = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Micro Computador'
        verbose_name_plural = 'Micros Computadores'

    def __unicode__(self):
        return self.model


class Equipment(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    model = models.CharField(max_length=100, verbose_name='Modelo')
    microComputer = models.ForeignKey('microComputer', verbose_name='Micro Computador')
    sensor = models.ForeignKey('Sensor', verbose_name='Sensor')
    expansion = models.ForeignKey('Expansion', verbose_name='Expansão')
    accessory = models.ForeignKey('Accessory', verbose_name='Acessório')
    userCreation = CreatingUserField(related_name="created_equipments")
    userAmendment = LastUserField()
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    dateTimeChange = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'

    def __unicode__(self):
        return self.name

class Sensor(models.Model):
    name = models.CharField(blank=True, max_length=100)
    
    class Meta:
        verbose_name = 'Sensor'
        verbose_name_plural = 'Sensores'
        
    def __unicode__(self):
        return self.name



class PhysicalCharacteristic(models.Model):
    microComputer = models.ForeignKey('microComputer', verbose_name='Micro Computador')
    length = models.CharField(blank=True, max_length=10, verbose_name='Comprimento')
    width = models.CharField(blank=True, max_length=10, verbose_name='Largura')
    weight = models.CharField(blank=True, max_length=10, verbose_name='Peso')
    
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
    type = models.CharField(blank=True, max_length=100, verbose_name='Tipo')
    clockSpeed = models.CharField(max_length=10, blank=True, verbose_name='Clock Speed')
    userCreation = CreatingUserField(related_name="created_gpus")
    userAmendment = LastUserField()
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    dateTimeChange = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'GPU'
        verbose_name_plural = 'GPUs'
        
    def __unicode__(self):
        return self.type


class Processor(models.Model):
    type = models.CharField(max_length=100, verbose_name='Processador')
    clockSpeed = models.CharField(blank=True, max_length=10, verbose_name='Clock Speed')
    userCreation = CreatingUserField(related_name="created_processor")
    userAmendment = LastUserField()
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    dateTimeChange = models.DateTimeField(auto_now=True)
    
    
    def __unicode__(self):
        return self.type

    class Meta:
        verbose_name = 'Processador'
        verbose_name_plural = 'Processadores'


class Microcontroller(models.Model):
    type = models.CharField(max_length=100, verbose_name='Microcontrolador')
    clockSpeed = models.CharField(blank=True, max_length=10, verbose_name='Clock Speed')
    userCreation = CreatingUserField(related_name="created_microcontroller")
    userAmendment = LastUserField()
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    dateTimeChange = models.DateTimeField(auto_now=True)
    
    
    def __unicode__(self):
        return self.type

    class Meta:
        verbose_name = 'Microcontrolador'
        verbose_name_plural = 'Microcontroladores'


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
    userCreation = CreatingUserField(related_name="created_operationsystems")
    userAmendment = LastUserField()
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    dateTimeChange = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Sistema Operativo'
        verbose_name_plural = 'Sistemas Operativos'
        
    def __unicode__(self):
        return self.name


class Expansion(models.Model):
    type = models.CharField(blank=True, max_length=100, verbose_name='Tipo')
    peripherals = models.CharField(blank=True, max_length=50, verbose_name='Periféricos')
    GPIO = models.IntegerField()
    userCreation = CreatingUserField(related_name="created_expansions")
    userAmendment = LastUserField()
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    dateTimeChange = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Expansão'
        verbose_name_plural = 'Expansões'
        
    def __unicode__(self):
        return self.type


class Accessory(models.Model):
    name = models.CharField(blank=True, max_length=100, verbose_name='Nome')
    type = models.CharField(blank=True, max_length=100, verbose_name='Tipo')
    userCreation = CreatingUserField(related_name="created_accessories")
    userAmendment = LastUserField()
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    dateTimeChange = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Acessório'
        verbose_name_plural = 'Acessórios'
        
    def __unicode__(self):
        return self.name


class Memory(models.Model):
    microComputer = models.ForeignKey('microComputer', verbose_name='Micro Computador')
    RAM = models.IntegerField(blank=True)
    SRAM = models.IntegerField(blank=True)
    EEPROM = models.IntegerField(blank=True)
    flashMemory = models.IntegerField(blank=True, verbose_name='Memória Flash')
    
    class Meta:
        verbose_name = 'Memória'
        verbose_name_plural = 'Memórias'

