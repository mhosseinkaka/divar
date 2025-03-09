from django.urls import path
from .views import jobs_s, technical, assistant, management

urlpatterns = [
    path('', jobs_s), 
    path('technial', technical),
    path('assitant', assistant),
    path('management', management)
]