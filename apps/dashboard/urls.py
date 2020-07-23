from django.urls import path

from .views import *

urlpatterns = [
    path('', dashboard, name = 'dashboard'),
    path('teste/<int:paciente_id>', teste, name = 'teste'),
]
