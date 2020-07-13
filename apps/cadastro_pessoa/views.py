from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Cliente, Paciente, Responsavel, Unidade
from datetime import datetime
from django.contrib import messages

from . import src


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
        return render(request, 'main_screen.html', data)
    else:
        return redirect('../usuarios/signin')


def page_protocolo(request, paciente_id):
    if request.user.is_authenticated:
        # try:
            paciente = get_object_or_404(Paciente, pk = paciente_id)
            if request.method == 'POST':
                novo_protocolo = request.POST.getlist('checks')
                protocolo = src.set_protocolos(paciente, novo_protocolo)
                paciente.protocolos=protocolo
                paciente.save()
                print(protocolo)

            data = {
                'paciente': paciente,
                'protocolos': src.get_protocolos(paciente),
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
                protocolo = src.set_protocolos(paciente, novo_protocolo)
                paciente.protocolos=protocolo
                paciente.save()
                print(protocolo)

            data = {
                'paciente': paciente,
                'protocolos': src.get_protocolos(paciente),
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


def page_form(request):
    data = {
        'meses': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio',
                   'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
                   'Novembro', 'Dezembro'],
        'anos': [str(datetime.now().year + i) for i in range(10)]
    }
    if request.user.is_authenticated:
        return render(request, 'pacientes/pages/page_form.html', data)
    else:
        return redirect('../usuarios/signin')


def page_form_paciente(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            nome = request.POST['nome']
            sobrenome = request.POST['sobrenome']
            email = request.POST['email']
            data_nascimento =  datetime.strptime(request.POST['data_nascimento'], "%d/%m/%Y").strftime("%Y-%m-%d")
            data_cadastro = datetime.now().strftime("%Y-%m-%d")
            phone = request.POST['phone']
            massa = request.POST['massa']
            estatura = request.POST['estatura']
            unidade = request.POST['unidade']
            responsavel = request.POST['responsavel']
            status = request.POST['status']
            genero = request.POST['genero']

            if src.validate_fields([nome, sobrenome, email, data_nascimento,
                                    phone, massa, estatura, unidade, responsavel,
                                    status, genero], request) and not src.pacient_exists(email, request):
                print(nome, sobrenome, email, data_nascimento, phone, massa, estatura, unidade,
                      responsavel, status, genero)

                pacient = Paciente.objects.create(
                    nome=nome,
                    sobrenome=sobrenome,
                    email=email,
                    data_nascimento=data_nascimento,
                    data_cadastro=data_cadastro,
                    telefone=phone,
                    massa_corporal=massa,
                    estatura=estatura,
                    unidade=Unidade.objects.get(cidade=unidade),
                    responsavel=Responsavel.objects.get(nome=responsavel),
                    status=status,
                    genero=genero,
                    protocolos='[]'
                )
                pacient.save()
                messages.success(request, 'SUCESSO!! Paciente cadastrado!,success')

                return redirect('table')

        data = {
            'unidades': Unidade.objects.all(),
            'responsaveis': Responsavel.objects.all()
        }
        return render(request, 'pacientes/pages/page_form_paciente.html', data)
    else:
        return redirect('../usuarios/signin')


def page_404(request):
    return render(request, 'error/page_404.html')


def page_500(request):
    return render(request, 'error/page_500.html')


def page_table(request):
    if request.user.is_authenticated:
        pacientes = Paciente.objects.all()
        opts = Paciente._meta
        informacoes = [f.name.replace('_', ' ').title() for f in sorted(opts.fields + opts.many_to_many)]

        data = {
            'pacientes': pacientes,
            'informacoes': informacoes
        }
        return render(request, 'pacientes/pages/page_table.html', data)
    else:
        return redirect('../usuarios/signin')


def error_404_view(request, exception):
    return render(request,'error/page_404.html')


def error_500_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'error/page_500.html', data)


def dicom_viewer(request):
    if request.user.is_authenticated:
        return render(request, 'pages/viewer.html')
    else:
        return redirect('../usuarios/signin')