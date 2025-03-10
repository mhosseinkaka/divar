from django.contrib import admin
from vehicles.models import Car, Truck, Vehicle, Motor
# Register your models here.
admin.site.register(Car)
admin.site.register(Truck)
admin.site.register(Vehicle)
admin.site.register(Motor)