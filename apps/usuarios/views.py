from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from cadastro_pessoa.models import Cliente, Paciente, Responsavel, Unidade
from datetime import datetime
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage

import os, uuid
from shutil import copyfile, rmtree

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
            user = authenticate(request, username=username, password=pwd)
            if user is not None:
                login(request, user)
                return redirect('tabela_pacientes')
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

            uuid_usuario = str(len(User.objects.all()))
            path_usuario = create_folder(uuid_usuario)

            try:
                arquivo_imagem = request.FILES['path_file']
                fs = FileSystemStorage()
                f = fs.save(os.path.join(path_usuario, 'image.png'), arquivo_imagem)
                path_imagem = os.path.join(path_usuario, 'image.png')
            except:
                path_imagem = ''

            user = User.objects.create_user(username=name, email=email, password=pwd)
            user.profile.path_imagem = path_imagem
            user.save()
            messages.success(request, 'SUCESSO!! Usuário cadastrado com sucesso!,success')
            return redirect('signin')
        else:
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
    return redirect('signin')


def create_folder(uuid_usuario):
    path_usuarios = os.path.join(settings.BASE_DIR, 'media', 'usuarios')
    if not(os.path.exists(path_usuarios)):
        os.mkdir(path_usuarios)
    path_usuario = os.path.join(path_usuarios, uuid_usuario)
    if not(os.path.exists(path_usuario)):
        os.mkdir(path_usuario)
    return path_usuario