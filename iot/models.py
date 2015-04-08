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

from audit_log.models.fields import CreatingUserField, LastUserField


class MicroComputer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    model = models.CharField(max_length=100, verbose_name='Modelo')
    processor = models.ForeignKey('Processor',  verbose_name='Processador')
    microcontroller = models.ForeignKey('Microcontroller',  verbose_name='Microcontrolador')
    GPU = models.ForeignKey('GPU', blank=True)
    operatingSystems = models.ForeignKey('OperatingSystem',  verbose_name='Sistema Operativo')
    dateManufacture = models.DateField( verbose_name='Data de Fabrico')
    userCreation = CreatingUserField(related_name="created_microcomputer")
    userAmendment = LastUserField()
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    dateTimeChange = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Microcomputador'
        verbose_name_plural = 'Microcomputadores'

    def __unicode__(self):
        return self.model


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Sensor'
        verbose_name_plural = 'Sensores'
        
    def __unicode__(self):
        return self.name


   

class PhysicalCharacteristic(models.Model):
    microComputer = models.ForeignKey('MicroComputer', verbose_name='Micro Computador')
    length = models.FloatField(default=0, verbose_name='Comprimento (mm)')
    width = models.FloatField(default=0, verbose_name='Largura (mm)')
    weight = models.FloatField(default=0, verbose_name='Peso (g)')
    
    class Meta:
        verbose_name = 'Característica Física'
        verbose_name_plural = 'Características Físicas'
        
    def __unicode__(self):
        return self.microComputer.model



class GPU(models.Model):
    type = models.CharField(max_length=100, verbose_name='Tipo')
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
    clockSpeed = models.CharField(max_length=10, verbose_name='Clock Speed')
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
    clockSpeed = models.CharField(max_length=10, verbose_name='Clock Speed')
    userCreation = CreatingUserField(related_name="created_microcontroller")
    userAmendment = LastUserField()
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    dateTimeChange = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Microcontrolador'
        verbose_name_plural = 'Microcontroladores'

    def __unicode__(self):
        return self.type


class Interface(models.Model):
    microComputer = models.ForeignKey('MicroComputer', verbose_name='Micro Computador')
    hdmi = models.CharField(blank=True, max_length=50)
    USBPorts = models.CharField(blank=True, max_length=50, verbose_name='Porta USB')
    videoInput = models.CharField(blank=True, max_length=50, verbose_name='Entrada de vídeo')
    videoOutputs = models.CharField(blank=True, max_length=50, verbose_name='Saida de vídeo')
    audioInputs = models.CharField(blank=True, max_length=50, verbose_name='Entrada de audio')
    audioOutputs = models.CharField(blank=True, max_length=50, verbose_name='Saida de audio')
    storage = models.CharField(blank=True, max_length=50, verbose_name='Armazenamento')
    network = models.CharField(blank=True, max_length=50, verbose_name='Rede')
    jack = models.CharField(blank=True, max_length=50)
    digitalIOPins = models.IntegerField(default=0, verbose_name='Pinos I/O digital')
    analogInputPins = models.IntegerField(default=0, verbose_name='Pinos de entrada analógica')
    
    class Meta:
        verbose_name = 'Interface'
        verbose_name_plural = 'Interfaces'
        
    def __unicode__(self):
        return self.microComputer.model
        

class OperatingSystem(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    version = models.CharField(blank=True, max_length=50, verbose_name='Versão')
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
    type = models.CharField(max_length=100, verbose_name='Tipo')
    peripherals = models.CharField(blank=True, max_length=50, verbose_name='Periféricos')
    GPIO = models.IntegerField(default=0)
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
    name = models.CharField(max_length=100, verbose_name='Nome')
    type = models.CharField(blank=True, max_length=100, verbose_name='Tipo')
    userCreation = CreatingUserField(related_name="created_accessory")
    userAmendment = LastUserField()
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    dateTimeChange = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Acessório'
        verbose_name_plural = 'Acessórios'
        
    def __unicode__(self):
        return self.name


class Memory(models.Model):
    microComputer = models.ForeignKey('MicroComputer', verbose_name='Micro Computador')
    
    MEGABIT = 'MG'
    KBIT = 'KB'
    MEMORIA = (
        (MEGABIT, 'MG'),
        (KBIT, 'KB'),
        
    )
    
    RAM = models.FloatField(default=0, verbose_name='RAM')
    quantidadeRAM = models.CharField(null=False, max_length=2, verbose_name='Quantidade em',
                                      choices=MEMORIA,
                                      default=KBIT)
    
    SRAM = models.FloatField(default=0, verbose_name='SRAM KB')
    EEPROM = models.FloatField(default=0, verbose_name='EEPROM KB')
    
    flashMemory = models.FloatField(default=0, verbose_name='Memória Flash')
    quantidadeFlashMemory = models.CharField(null=False, max_length=2, verbose_name='Quantidade em',
                                      choices=MEMORIA,
                                      default=KBIT)
    
    class Meta: 
        verbose_name = 'Memória'
        verbose_name_plural = 'Memórias'
        
    def __unicode__(self):
        return self.microComputer.model

class Voltage(models.Model):
    microComputer = models.ForeignKey('MicroComputer', verbose_name='Micro Computador')
    operatingVoltage = models.IntegerField(default=0, verbose_name='Voltagem Operacional')
    IOCurrentMax = models.IntegerField(default=0, verbose_name='I/O Corrente máxima')
    inputVoltageRecommended = models.IntegerField(default=0, verbose_name='Voltagem recomendada')
    DCCurrentperIOPin = models.IntegerField(default=0, verbose_name='DC Corrente por pino')
    DCCurrentfor3_3VPin = models.IntegerField(default=0, verbose_name='DC Corrente por 3.3 pino')
    powerRatings = models.CharField(blank=True, max_length=50, verbose_name='Classificações de energia')
    powerSource = models.CharField(blank=True, max_length=50, verbose_name='Fonte de energia')
    
    class Meta:
        verbose_name = 'Voltagem'
        verbose_name_plural = 'Voltagens'
        
    def __unicode__(self):
        return self.microComputer.model

class Equipment(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    model = models.CharField(blank=True, max_length=100, verbose_name='Modelo')
    microComputer = models.ForeignKey('MicroComputer', verbose_name='Micro Computador')
    sensor = models.ManyToManyField('Sensor', blank=True, verbose_name = 'Sensor')
    expansion = models.ManyToManyField('Expansion', blank=True, verbose_name = 'Expansão')
    accessory = models.ManyToManyField('Accessory', blank=True, verbose_name = 'Acessório')
    userCreation = CreatingUserField(related_name="created_equipments")
    userAmendment = LastUserField()
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    dateTimeChange = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'

    def __unicode__(self):
        return self.name
