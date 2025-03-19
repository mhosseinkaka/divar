from django.contrib.admin import ModelAdmin, register
from vehicles.models import Car, Truck, Motor, Vehicle
# Register your models here.
@register(Car)
class Caradmin(ModelAdmin):
    list_display = ['name', 'brand']

@register(Truck)
class Truckadmin(ModelAdmin):
    list_display = ['name', 'brand']


@register(Motor)
class Motoradmin(ModelAdmin):
    list_display = ['name', 'brand']

@register(Vehicle)
class Vehicleadmin(ModelAdmin):
    list_display = ['engine', 'cc', 'sokht', 'vazn', 'number_sarneshin', 'country_product']
