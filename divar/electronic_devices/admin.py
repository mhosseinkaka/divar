from django.contrib.admin import ModelAdmin, register
from electronic_devices.models import *
# Register your models here.

@register(E_device)
class E_deviceAdmin(ModelAdmin):
    list_display = ['name', 'power', 'product_year', 'price']

@register(Tablet)
class TabletAdmin(ModelAdmin):
    list_display = ['brand', 'name', 'product_year', 'price']

@register(Mobile)
class MobileAdmin(ModelAdmin):
    list_display = ['brand', 'name', 'product_year', 'price']

@register(Computers)
class ComputersAdmin(ModelAdmin):
    list_display = ['brand', 'name', 'product_year', 'price']

@register(Game_console)
class Game_consoleAdmin(ModelAdmin):
    list_display = ['brand', 'name', 'product_year', 'price']

@register(Video_audio)
class Video_audioAdmin(ModelAdmin):
    list_display = ['brand', 'name', 'product_year', 'price']
