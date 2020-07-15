from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from cadastro_pessoa.models import Cliente, Paciente, Responsavel, Unidade
from datetime import datetime
from django.contrib import messages
from django.conf import settings

import os


def index(request):
    if request.user.is_authenticated:
        pacientes = Paciente.objects.all()
        usuarios = User.objects.all()
        responsaveis = Responsavel.objects.all()

        data = {
            'pacientes': pacientes,
            'usuarios': usuarios,
            'responsaveis': responsaveis
        }
        return render(request, 'dashboard/page_dashboard.html', data)
    else:
        return redirect('../usuarios/signin')