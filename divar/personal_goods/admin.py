from django.contrib.admin import ModelAdmin, register
from personal_goods.models import Shoes, Clothe, Detail
# Register your models here.
@register(Shoes)
class ShoesAdmin(ModelAdmin):
    list_display = ['brand', 'size', 'price']

@register(Clothe)
class ClotheAdmin(ModelAdmin):
    list_display = ['brand', 'size', 'price']

@register(Detail)
class DetailAdmin(ModelAdmin):
    list_display = ['name', 'product_owner', 'price']