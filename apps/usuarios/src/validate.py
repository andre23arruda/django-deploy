from django.contrib.auth.models import User
from django.contrib import messages

def validate_name(name, request):
    if not name.strip():
        print('ERRO!! Nome em branco!')
        messages.error(request, 'ERRO!! Nome em branco!,error')
        return False
    return True

def validate_email(email, request):
    if not email.strip():
        print('ERRO!! Email em branco!')
        messages.error(request, 'ERRO!! Email em branco!,error')
        return False
    return True

def validate_password(password, password_cofirm, request):
    if password.strip() and password == password_cofirm:
        return True
    print('ERRO!! Verifique a senha!')
    messages.error(request, 'ERRO!! Verifique a senha!,error')
    return False

def validate_user(email, request):
    if User.objects.filter(email=email):
        print('ERRO!! Usuário já cadastrado!')
        messages.error(request, 'ERRO!! Usuário já cadastrado!,error')
        return False
    return True