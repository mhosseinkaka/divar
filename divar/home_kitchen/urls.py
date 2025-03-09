from django.urls import path
from .views import home_kitchen

urlpatterns = [
    path('<str:objects>', home_kitchen)
]