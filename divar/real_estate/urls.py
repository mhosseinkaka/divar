from django.urls import path
from .views import makan, makan_edari, makan_sell

urlpatterns = [
    path('', makan),
    path('makan-sell', makan_sell),
    path('makan-edari', makan_edari)
]