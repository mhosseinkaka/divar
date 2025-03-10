from django.urls import path
from .views import car, motorcycle, truck

urlpatterns = [
    path('car', car),
    path('truck', truck),
    path('motor', motorcycle)
]