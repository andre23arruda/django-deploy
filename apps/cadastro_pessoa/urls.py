from django.urls import path

from .views import *

urlpatterns = [
    path('view_protocolo/<int:paciente_id>', view_protocolo, name = 'view_protocolo'),
    path('edit_protocolo/<int:paciente_id>/<str:data_exame>', edit_protocolo, name = 'edit_protocolo'),
    path('delete_protocolo/<int:paciente_id>/<str:data_exame>/<str:nome_protocolo>', delete_protocolo, name = 'delete_protocolo'),
    path('delete_paciente/<int:paciente_id>', delete_paciente, name = 'delete_paciente'),
    path('edit_paciente/<int:paciente_id>', edit_paciente, name = 'edit_paciente'),
    path('form', page_form, name = 'form'),
    path('create_paciente',create_paciente, name = 'create_paciente'),
    path('tabela_pacientes', tabela_pacientes, name = 'tabela_pacientes'),
    path('print_paciente/<int:paciente_id>', print_paciente, name = 'print_paciente'),
]
