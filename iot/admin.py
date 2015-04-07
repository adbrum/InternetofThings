from django.contrib import admin

from iot.models import Processor, MicroComputer, PhysicalCharacteristic, Voltage, \
GPU, OperatingSystem, Interface, Expansion, Accessory, Memory, Equipment, Sensor, Microcontroller


admin.site.register(Equipment)
admin.site.register(Processor)

class MicroComputerAdmin(admin.ModelAdmin):
    list_display = ('model', 'name')

admin.site.register(MicroComputer, MicroComputerAdmin)

class MicrocontrollerAdmin(admin.ModelAdmin):
    list_display = ('type', 'clockSpeed')
    
admin.site.register(Microcontroller, MicrocontrollerAdmin)

admin.site.register(PhysicalCharacteristic)
admin.site.register(GPU)
admin.site.register(OperatingSystem)
admin.site.register(Interface)
admin.site.register(Expansion)
admin.site.register(Accessory)
admin.site.register(Memory)
admin.site.register(Sensor)
admin.site.register(Voltage)
