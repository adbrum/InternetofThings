from iot.models import Processor, MicroComputador, PhysicalCharacteristics, Voltage, \
GPU, OperationSystem,Interfaces, Expansion, Accessory, Memory, Equipment

from django.contrib import admin

admin.site.register(Equipment)
admin.site.register(Processor)
admin.site.register(MicroComputador)
admin.site.register(PhysicalCharacteristics)
admin.site.register(GPU)
admin.site.register(OperationSystem)
admin.site.register(Interfaces)
admin.site.register(Expansion)
admin.site.register(Accessory)
admin.site.register(Memory)

