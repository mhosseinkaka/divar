from django.urls import path
from .views import *

urlpatterns = [
    path('', personal_goods),
    path('apparel', apparel),
    path('accessories', accessories),
    path('beauty', beauty),
    path('child-apparel', child_apparel),
    path('child-product', child_product),
    path('stationery',stationery)
]