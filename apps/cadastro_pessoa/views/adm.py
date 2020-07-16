from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from cadastro_pessoa.models import Cliente, Paciente, Responsavel, Unidade
from datetime import datetime
from django.contrib import messages
from django.conf import settings

import os
import json


def dashboard(request):
    if request.user.is_authenticated:
        pacientes = Paciente.objects.all()
        usuarios = User.objects.all()
        responsaveis = Responsavel.objects.all()

        meses = {'jan': '01', 'fev': '02', 'mar': '03', 'abr': '04',
                 'mai': '05', 'jun': '06', 'jul': '07', 'ago': '08',
                 'set': '09', 'out': '10', 'nov': '11', 'dez': '12'}
        ano_atual = str(datetime.now().year)

        count_exames = {}
        for mes, mes_numero in meses.items():
            count_exames[mes] = len(pacientes.filter(protocolos__icontains='/'.join([mes_numero, ano_atual])))
        print(count_exames)

        data = {
            'pacientes': pacientes,
            'usuarios': usuarios,
            'responsaveis': responsaveis,
            'count_exames': count_exames
        }
        return render(request, 'dashboard/page_dashboard.html', data)
    else:
        return redirect('signin')