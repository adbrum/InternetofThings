# -*- coding: utf-8 -*-
"""
Nome Autor: Adriano Leal
nº Aluno: 11951
911911951@alunos.ipbeja.pt
"""
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class Equipment(models.Model):
    processor = models.ForeignKey('Processor')
    GPU = models.ForeignKey('GPU')
    operationSystem = models.ForeignKey('OperationSystem')
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    dateManufacture = models.DateField()
    dateTimeCreation = models.DateTimeField(null=True)
    userCreation = models.CharField(null=True, max_length=50)
    dateTimeChange = models.DateTimeField(null=True)
    userAmendment = models.CharField(null=True, max_length=50)

    def __str__(self):
        return self.name


class PhysicalCharacteristics(models.Model):
    equipment = models.ForeignKey('Equipment')
    length = models.FloatField()
    width = models.FloatField()
    weight = models.IntegerField()


class Voltage(models.Model):
    equipment = models.ForeignKey('Equipment')
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
    userCreation = models.CharField(null=True, max_length=50)
    userAmendment = models.CharField(null=True, max_length=50)
    dateTimeCreation = models.DateTimeField(null=True)
    dateTimeChange = models.DateTimeField(null=True)


class Processor(models.Model):
    type = models.CharField(max_length=100)
    clockSpeed = models.IntegerField()
    dateTimeCreation = models.DateTimeField(null=True)
    userCreation = models.CharField(null=True, max_length=50)
    dateTimeChange = models.DateTimeField(null=True)
    userAmendment = models.CharField(null=True, max_length=50)


class Interfaces(models.Model):
    equipment = models.ForeignKey('Equipment')
    hdmi = models.BooleanField(default=False)
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
    dateTimeCreation = models.DateTimeField(null=True)
    userCreation = models.CharField(null=True, max_length=50)
    dateTimeChange = models.DateTimeField(null=True)
    userAmendment = models.CharField(null=True, max_length=50)


class Expansion(models.Model):
    equipment = models.ForeignKey('Equipment')
    peripherals = models.CharField(max_length=50)
    GPIO = models.IntegerField()


class Accessories(models.Model):
    equipment = models.ForeignKey('Equipment')
    type = models.CharField(max_length=100)


class Memory(models.Model):
    equipment = models.ForeignKey('Equipment')
    RAM = models.IntegerField()
    SRAM = models.IntegerField()
    EEPROM = models.IntegerField()
    flashMemory = models.IntegerField()

