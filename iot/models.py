# -*- coding: utf-8 -*-
"""
Nome Autor: Adriano Leal
nº Aluno: 11951
911911951@alunos.ipbeja.pt
"""
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


now = datetime.now()

class Equipment(models.Model):
    microComputador = models.ForeignKey('MicroComputador')
    operationSystem = models.ForeignKey('OperationSystem')
    Sensors = models.ForeignKey('Sensors')
    expansion = models.ForeignKey('Expansion')
    accessory = models.ForeignKey('Accessory')
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    dateManufacture = models.DateField()
    dateTimeCreation = now
    userCreation = models.CharField(max_length=100)
    dateTimeChange = now
    userAmendment = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Sensors(models.Model):
    name = models.CharField(max_length=100)


class MicroComputador(models.Model):
    processor = models.ForeignKey('Processor')
    GPU = models.ForeignKey('GPU')
    operationSystem = models.ForeignKey('OperationSystem')
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    dateManufacture = models.DateField()
    dateTimeCreation = now
    userCreation = models.CharField(max_length=100)
    dateTimeChange = now
    userAmendment = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class PhysicalCharacteristics(models.Model):
    MicroComputador = models.ForeignKey('MicroComputador')
    length = models.FloatField()
    width = models.FloatField()
    weight = models.IntegerField()


class Voltage(models.Model):
    MicroComputador = models.ForeignKey('MicroComputador')
    operatingVoltage = models.IntegerField()
    IOCurrentMax = models.IntegerField()
    inputVoltageRecommended = models.IntegerField()
    DCCurrentperIOPin = models.IntegerField()
    DCCurrentfor3_3VPin = models.IntegerField()
    powerRatings = models.CharField(max_length=50)
    powerSource = models.CharField(max_length=50)


class GPU(models.Model):
    type = models.CharField(max_length=100)
    clockSpeed = models.IntegerField()
    dateTimeCreation = now
    userCreation = models.CharField(max_length=100)
    dateTimeChange = now
    userAmendment = models.CharField(max_length=100)


class Processor(models.Model):
    type = models.CharField(max_length=100)
    clockSpeed = models.IntegerField()
    dateTimeCreation = now
    userCreation = models.CharField(max_length=100)
    dateTimeChange = now
    userAmendment = models.CharField(max_length=100)


class Interfaces(models.Model):
    MicroComputador = models.ForeignKey('MicroComputador')
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


class OperationSystem(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    dateTimeCreation = now
    userCreation = models.CharField(max_length=100)
    dateTimeChange = now
    userAmendment = models.CharField(max_length=100)


class Expansion(models.Model):
    type = models.CharField(max_length=100)
    peripherals = models.CharField(max_length=50)
    GPIO = models.IntegerField()


class Accessory(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)


class Memory(models.Model):
    MicroComputador = models.ForeignKey('MicroComputador')
    RAM = models.IntegerField()
    SRAM = models.IntegerField()
    EEPROM = models.IntegerField()
    flashMemory = models.IntegerField()

