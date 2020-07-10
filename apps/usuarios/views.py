from django.shortcuts import render, redirect, get_list_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings


from . import src

def page_signin(request):
    '''Usuário entra no sistema'''
    if request.method == 'POST':
        email = request.POST['username']
        pwd = request.POST['pwd']
        username = src.authentication_email(email, request)

        if not username:
            username = src.authentication_username(email, request)

        if username:
            print(username)
            user = authenticate(request, username=username, password=pwd)
            if user is not None:
                login(request, user)
                print('Login realizado com sucesso')
                return redirect('../pacientes/table')
            messages.error(request, 'ERRO!! Senha errada!,error')

        return redirect('signin')

    return render(request, 'usuarios/pages/page_signin.html')


def page_signup(request):
    ''' Validação das informações e usuário se cadastra no sistema '''

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        pwd = request.POST['pwd']
        pwd_confirm = request.POST['pwd_confirm']

        result = src.recaptcha(request)

        if result['success'] and src.validate_name(name, request) and src.validate_password(pwd, pwd_confirm, request) and src.validate_email(email, request) and src.validate_user(email, request):
            user = User.objects.create_user(username=name, email=email, password=pwd)
            user.save()
            print('Usuário cadastrado com sucesso')
            messages.success(request, 'SUCESSO!! Usuário cadastrado com sucesso!,success')
            return redirect('signin')
        else:
            print(messages.error)
            return redirect('signup')
    return render(request, 'usuarios/pages/page_signup.html', {'site_key': settings.RECAPTCHA_SITE_KEY})


def page_user_profile(request):
    ''' Página de perfil do usuário '''
    if request.user.is_authenticated:
        return render(request, 'usuarios/pages/page_user_profile.html')
    else:
        return redirect('signin')


def user_logout(request):
    ''' Usuário sai do sistema '''
    logout(request)
    print('LOGOUT')
    return redirect('signin')
