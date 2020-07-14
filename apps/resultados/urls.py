from django.urls import path
from . import views

urlpatterns = [
    path('', views.resultado_signin, name = ''),
    path('resultado_signin', views.resultado_signin, name = 'resultado_signin'),
    path('resultado_table', views.resultado_table, name = 'resultado_table'),
    path('teste', views.teste, name = 'teste'),
]