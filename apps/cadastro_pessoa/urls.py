from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('protocolo/<int:paciente_id>', views.page_protocolo, name = 'protocolo'),
    path('protocolo_view/<int:paciente_id>', views.page_protocolo_view, name = 'protocolo_view'),
    path('delete_paciente/<int:paciente_id>', views.delete_paciente, name = 'delete_paciente'),
    path('edit_paciente/<int:paciente_id>', views.edit_paciente, name = 'edit_paciente'),
    path('form', views.page_form, name = 'form'),
    path('form_paciente', views.page_form_paciente, name = 'form_paciente'),
    path('table', views.page_table, name = 'table'),
    path('dicom_viewer', views.dicom_viewer, name = 'dicom_viewer')
]
