"""
Adriano Leal
11951
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
    model = models.CharField(max_length=100)
    dateManufacture = models.DateField()
    typeModel = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    clockSpeed = models.IntegerField()
    length = models.FloatField()
    width = models.FloatField()
    weight = models.IntegerField()
    RAM = models.IntegerField()
    GPIO = models.IntegerField()
    IOCurrentMax = models.CharField(max_length=10)
    power = models.IntegerField()


class Arduino(Equipment):
    # microcontroller = models.CharField(max_length=100)
    operatingVoltage = models.IntegerField()
    inputVoltageRecommended = models.IntegerField()
    digitalIOPins = models.IntegerField()
    analogInputPins = models.IntegerField()
    DCCurrentperIOPin = models.IntegerField()
    DCCurrentfor3_3VPin = models.IntegerField()
    flashMemory = models.IntegerField()
    SRAM = models.IntegerField()
    EEPROM = models.IntegerField()


class RasperryPI(Equipment):
    operatingSystem = models.CharField(max_length=50)
    GPU = models.CharField(max_length=50)
    USBPorts = models.CharField(max_length=50)
    videoInput = models.CharField(max_length=50)
    videoOutputs = models.CharField(max_length=50)
    audioInputs = models.CharField(max_length=50)
    audioOutputs = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    peripherals = models.CharField(max_length=50)
    powerRatings = models.CharField(max_length=50)
    powerSource = models.CharField(max_length=50)