from django.urls import path
from .views import entertainment, ticket, tour, books, scoter, animal, music, sport, toys

urlpatterns = [
    path('', entertainment),
    path('ticket/<str:place>', ticket),
    path('tour/<str:city_name>', tour),
    path('books/', books),
    path('scoter/', scoter),
    path('animal/', animal),
    path('music/', music),
    path('sport/', sport),
    path('toys/', toys),
]