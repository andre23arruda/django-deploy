from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from cadastro_pessoa.models import Cliente, Paciente, Responsavel, Unidade
from datetime import datetime
from django.contrib import messages
from django.conf import settings
import json

import os

from cadastro_pessoa.src import set_protocolos, get_protocolos


def page_protocolo(request, paciente_id):
    if request.user.is_authenticated:
        # try:
            paciente = get_object_or_404(Paciente, pk = paciente_id)
            if request.method == 'POST':
                novo_protocolo = request.POST.getlist('checks')
                protocolo = set_protocolos(paciente, novo_protocolo)
                paciente.protocolos=protocolo
                paciente.save()
                print(protocolo)

            data = {
                'paciente': paciente,
                'protocolos': get_protocolos(paciente),
                'protocolos_nome_col1':{
                    'anamnese': 'Anamnese',
                    'lombar': 'Lombar e Quadril',
                    'joelho': 'Joelho',
                    'tornozelo': 'Tornozelo',
                    'corrida': 'Corrida',
                    'futebol': 'Futebol',
                    'tenis': 'Tênis',
                    'basquete': 'Basquete'},
                'protocolos_nome_col2':{
                    'voleibol': 'Voleibol',
                    'prancha': 'Prancha',
                    'idosos': 'Idosos',
                    'ombro': 'Ombro',
                    'cervical': 'Cervical',
                    'cotovelo': 'Cotovelo',
                    'equilibrio': 'Equilíbrio'
                }
            }

            return render(request, 'pacientes/pages/page_protocolo.html', data)

        # except:
        #     return redirect('table')
    else:
        return redirect('../usuarios/signin')


def page_protocolo_view(request, paciente_id):
    if request.user.is_authenticated:
        # try:
            paciente = get_object_or_404(Paciente, pk = paciente_id)
            if request.method == 'POST':
                novo_protocolo = request.POST.getlist('checks')
                protocolo = set_protocolos(paciente, novo_protocolo)
                paciente.protocolos = protocolo
                paciente.save()
                print(protocolo)

            data = {
                'paciente': paciente,
                'protocolos': get_protocolos(paciente),
                'protocolos_nome_col1':{
                    'anamnese': 'Anamnese',
                    'lombar': 'Lombar e Quadril',
                    'joelho': 'Joelho',
                    'tornozelo': 'Tornozelo',
                    'corrida': 'Corrida',
                    'futebol': 'Futebol',
                    'tenis': 'Tênis',
                    'basquete': 'Basquete'},
                'protocolos_nome_col2':{
                    'voleibol': 'Voleibol',
                    'prancha': 'Prancha',
                    'idosos': 'Idosos',
                    'ombro': 'Ombro',
                    'cervical': 'Cervical',
                    'cotovelo': 'Cotovelo',
                    'equilibrio': 'Equilíbrio'
                }
            }

            return render(request, 'pacientes/pages/page_protocolo_view.html', data)

        # except:
        #     return redirect('table')
    else:
        return redirect('../usuarios/signin')


def protocolo_edit(request, paciente_id, data_exame):

    if request.method == 'POST':
        paciente = get_object_or_404(Paciente, pk = paciente_id)
        protocolos = get_protocolos(paciente)
        data_exame_replace = data_exame.replace('_', '/')
        protocolos_exame = protocolos[data_exame_replace]

        for protocolo in protocolos_exame.keys():
            protocolos[data_exame_replace][protocolo] = request.POST.getlist(data_exame + '_' + protocolo)
            print('='*30)
            print(request.POST.getlist(data_exame + '_' + protocolo))

        protocolos = json.dumps(protocolos)
        paciente.protocolos = protocolos
        paciente.save()

    return redirect('../../protocolo_view/' + str(paciente_id))
