from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name = 'index'),
    path('protocolo/<int:paciente_id>', page_protocolo, name = 'protocolo'),
    path('protocolo_view/<int:paciente_id>', page_protocolo_view, name = 'protocolo_view'),
    path('protocolo_edit/<int:paciente_id>/<str:data_exame>', protocolo_edit, name = 'protocolo_edit'),
    path('delete_paciente/<int:paciente_id>', delete_paciente, name = 'delete_paciente'),
    path('edit_paciente/<int:paciente_id>', edit_paciente, name = 'edit_paciente'),
    path('form', page_form, name = 'form'),
    path('form_paciente', page_form_paciente, name = 'form_paciente'),
    path('table', page_table, name = 'table'),
    path('dicom_viewer', dicom_viewer, name = 'dicom_viewer')
]
