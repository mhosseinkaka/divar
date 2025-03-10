from django.urls import path
from .views import material

urlpatterns = [
    path('', material)
]