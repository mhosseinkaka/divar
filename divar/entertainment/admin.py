from django.contrib import admin
from entertainment.models import Entertainment, Ticket, Event, Tour, Book, Scoter
# Register your models here.

admin.site.register(Entertainment)
admin.site.register(Ticket)
admin.site.register(Tour)
admin.site.register(Event)
admin.site.register(Book)
admin.site.register(Scoter)
