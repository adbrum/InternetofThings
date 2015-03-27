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
    processor = models.ForeignKey('Processor', verbose_name=_('processor'))
    GPU = models.ForeignKey('GPU')
    operationSystem = models.ForeignKey('OperationSystem')
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    dateManufacture = models.DateField()
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    userCreation = models.CharField(max_length=100)
    dateTimeChange = models.DateTimeField(auto_now=True)
    userAmendment = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Micro Computador'
        verbose_name_plural = 'Micro Computador'

    def __unicode__(self):
        return self.name


class Equipment(models.Model):
    microComputer = models.ForeignKey('microComputer')
    operationSystem = models.ForeignKey('OperationSystem')
    sensor = models.ForeignKey('Sensor')
    expansion = models.ForeignKey('Expansion')
    accessory = models.ForeignKey('Accessory')
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    dateManufacture = models.DateField()
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    userCreation = models.CharField(max_length=100)
    dateTimeChange = models.DateTimeField(auto_now=True)
    userAmendment = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamento'

    def __unicode__(self):
        return self.name

class Sensor(models.Model):
    name = models.CharField(max_length=100)



class PhysicalCharacteristic(models.Model):
    microComputer = models.ForeignKey('microComputer')
    length = models.FloatField()
    width = models.FloatField()
    weight = models.IntegerField()
    
    class Meta:
        verbose_name = 'Característica Física'
        verbose_name_plural = 'Característica Física'


class Voltage(models.Model):
    microComputer = models.ForeignKey('microComputer')
    operatingVoltage = models.IntegerField()
    IOCurrentMax = models.IntegerField()
    inputVoltageRecommended = models.IntegerField()
    DCCurrentperIOPin = models.IntegerField()
    DCCurrentfor3_3VPin = models.IntegerField()
    powerRatings = models.CharField(max_length=50)
    powerSource = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Voltagem'
        verbose_name_plural = 'Voltagem'


class GPU(models.Model):
    type = models.CharField(max_length=100)
    clockSpeed = models.IntegerField()
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    userCreation = models.CharField(max_length=100)
    dateTimeChange = models.DateTimeField(auto_now=True)
    userAmendment = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'GPU'
        verbose_name_plural = 'GPU'


class Processor(models.Model):
    type = models.CharField(max_length=100)
    clockSpeed = models.IntegerField()
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    userCreation = models.CharField(max_length=100)
    dateTimeChange = models.DateTimeField(auto_now=True)
    userAmendment = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Processador'
        verbose_name_plural = 'Processador'


class Interface(models.Model):
    microComputer = models.ForeignKey('microComputer')
    hdmi = models.CharField(max_length=50)
    USBPorts = models.CharField(max_length=50)
    videoInput = models.CharField(max_length=50)
    videoOutputs = models.CharField(max_length=50)
    audioInputs = models.CharField(max_length=50)
    audioOutputs = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    jack = models.CharField(max_length=50)
    digitalIOPins = models.IntegerField()
    analogInputPins = models.IntegerField()
    
    class Meta:
        verbose_name = 'Interface'
        verbose_name_plural = 'Interface'


class OperationSystem(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    userCreation = models.CharField(max_length=100)
    dateTimeChange = models.DateTimeField(auto_now=True)
    userAmendment = models.CharField(max_length=100)


class Expansion(models.Model):
    type = models.CharField(max_length=100)
    peripherals = models.CharField(max_length=50)
    GPIO = models.IntegerField()
    
    class Meta:
        verbose_name = 'Expansão'
        verbose_name_plural = 'Expansão'


class Accessory(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Acessório'
        verbose_name_plural = 'Acessório'


class Memory(models.Model):
    microComputer = models.ForeignKey('microComputer')
    RAM = models.IntegerField()
    SRAM = models.IntegerField()
    EEPROM = models.IntegerField()
    flashMemory = models.IntegerField()
    
    class Meta:
        verbose_name = 'Memória'
        verbose_name_plural = 'Memória'

