from django.contrib.admin import ModelAdmin, register
from entertainment.models import Entertainment, Ticket, Event, Tour, Book, Scoter
# Register your models here.

@register(Entertainment)
class EntertainmentAdmin(ModelAdmin):
    list_display = ['title', 'created_at']

@register(Ticket)
class TicketAdmin(ModelAdmin):
    list_display = ['title', 'created_at', 'place']

@register(Tour)
class TourAdmin(ModelAdmin):
    list_display = ['title', 'start', 'city_name', 'place']

@register(Event)
class EventAdmin(ModelAdmin):
    list_display = ['title', 'place']

@register(Book)
class BookAdmin(ModelAdmin):
    list_display = ['title', 'author']

@register(Scoter)
class ScoterAdmin(ModelAdmin):
    list_display = ['title', 'price', 'size', 'model_device']