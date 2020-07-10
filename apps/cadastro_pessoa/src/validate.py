from ..models import Paciente
from django.contrib import messages

def validate_fields(fields, request):
    for field in fields:
        if not field.strip():
            print('ERRO!! Faltando informação!')
            messages.error(request, 'ERRO!! Faltando informação!,error')
            return False
    return True

def pacient_exists(email, request):
    if Paciente.objects.filter(email=email):
        print('ERRO!! Paciente já cadastrado!')
        messages.error(request, 'ERRO!! Paciente já cadastrado!,error')
        return True
    return False