from iot.models import Processor, MicroComputer, PhysicalCharacteristic, Voltage, \
GPU, OperationSystem,Interface, Expansion, Accessory, Memory, Equipment

from django.contrib import admin

admin.site.register(Equipment)
admin.site.register(Processor)
admin.site.register(MicroComputer)
admin.site.register(PhysicalCharacteristic)
admin.site.register(GPU)
admin.site.register(OperationSystem)
admin.site.register(Interface)
admin.site.register(Expansion)
admin.site.register(Accessory)
admin.site.register(Memory)

