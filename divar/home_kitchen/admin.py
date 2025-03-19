from django.contrib.admin import ModelAdmin, register
from home_kitchen.models import Home_object
# Register your models here.
@register(Home_object)
class Home_objectAdmin(ModelAdmin):
    list_display = ['name', 'year', 'weight', 'price', 'creator', 'place']