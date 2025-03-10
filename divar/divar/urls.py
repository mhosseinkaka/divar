"""
URL configuration for divar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('electronic-devices/', include('electronic_devices.urls')),
    path('entertainment/', include('entertainment.urls')),
    path('home-kitchen/', include('home_kitchen.urls')),
    path('jobs/', include('job_s.urls')),
    path('personal-goods', include('personal_goods.urls')),
    path('real-state', include('real_estate.urls')),
    path('servises/', include('service_s.urls')),
    path('social-services', include('social_services.urls')),
    path('tools-materials-equipment', include('tools_materials_equipment.urls')),
    path('vehicles', include('vehicles.urls'))
]
