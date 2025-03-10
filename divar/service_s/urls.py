from django.urls import path
from .views import service, vehicles_services, catering_services, technology_services, financial_services, transport_logistic_services

urlpatterns = [
    path('', service),
    path('vehicles-services', vehicles_services),
    path('catering-services', catering_services),
    path('technology-services', technology_services),
    path('financial-services', financial_services),
    path('transport-logistic-services', transport_logistic_services)
]