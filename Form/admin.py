from django.contrib import admin
from .models import Form, Device, Manufacture, Master

@admin.register(Manufacture)
class ManufactureAdmin(admin.ModelAdmin):
    
    list_display = ('manufacture',)
    
    fields = ['manufacture']

@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    
    list_display = ('last_name', 'first_name')
    
    fields = [('last_name', 'first_name')]
    
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    
    list_display = ('type',)
    
    fields = ['type']
    
@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    
    list_display = ('last_name', 'first_name',
                     'phone', 
                     'type', 'manufacture','model',
                     'reason', 'is_repairable',
                      'price',
                      'password',
                      'serial_number',
                      'took_the_order',
                      'open_order',
                      'done_order')
    
    fields = [('last_name', 'first_name'),
                     'phone', 
                     ('type','manufacture', 'model'),
                     ('reason','is_repairable'),
                      'price',
                      'password',
                      'serial_number',
                      'took_the_order',
                      ('open_order', 'done_order')]
    
    list_filter = ('manufacture', 'type', 'open_order', 'took_the_order')
    