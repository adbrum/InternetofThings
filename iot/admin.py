from django.contrib import admin

from iot.models import Processor, MicroComputer, PhysicalCharacteristic, Voltage, \
GPU, OperatingSystem, Interface, Expansion, Accessory, Memory, Equipment, Sensor


admin.site.register(Equipment)
admin.site.register(Processor)
admin.site.register(MicroComputer)
admin.site.register(PhysicalCharacteristic)
admin.site.register(GPU)
admin.site.register(OperatingSystem)
admin.site.register(Interface)
admin.site.register(Expansion)
admin.site.register(Accessory)
admin.site.register(Memory)
admin.site.register(Sensor)


class ProcessorAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'added_by', None) is None:
            obj.added_by = request.user
        obj.last_modified_by = request.user
        obj.save()