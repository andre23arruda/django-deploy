from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from cadastro_pessoa.models import Cliente, Paciente, Responsavel, Unidade
from datetime import datetime
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage

import os, uuid
from shutil import copyfile, rmtree
from cadastro_pessoa.src import validate_fields, pacient_exists

nome_empresa = 'BIOCINETICA'

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
        return redirect('/signin')


def create_paciente(request):
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

            if validate_fields([nome, sobrenome, email, data_nascimento,
                                phone, massa, estatura, unidade, responsavel,
                                status, genero], request) and not pacient_exists(email, request):
                print(nome, sobrenome, email, data_nascimento, phone, massa, estatura, unidade,
                      responsavel, status, genero)

                uuid_paciente = nome_empresa + '_' + uuid.uuid4().hex
                path_paciente = create_folder(uuid_paciente)

                try:
                    arquivo_imagem = request.FILES['path_imagem']
                    fs = FileSystemStorage()
                    f = fs.save(os.path.join(path_paciente, 'image.png'), arquivo_imagem)
                    path_imagem = os.path.join(path_paciente, 'image.png')
                except:
                    path_imagem = ''

                protocolos = os.path.join(path_paciente, 'protocolos.json')
                with open(protocolos, 'w') as fp:
                    fp.write("{}")

                paciente = Paciente.objects.create(
                    nome = nome,
                    sobrenome = sobrenome,
                    email = email,
                    data_nascimento = data_nascimento,
                    data_cadastro = data_cadastro,
                    telefone = phone,
                    massa_corporal = massa,
                    estatura = estatura,
                    unidade = Unidade.objects.get(cidade = unidade),
                    responsavel = Responsavel.objects.get(nome = responsavel),
                    status = status,
                    genero = genero,
                    path_imagem = path_imagem,
                    protocolos = "{}",
                    uuid_paciente = uuid_paciente
                )

                paciente.save()
                messages.success(request, 'SUCESSO!! Paciente cadastrado!,success')

                return redirect('tabela_pacientes')

        data = {
            'unidades': Unidade.objects.all(),
            'responsaveis': Responsavel.objects.all()
        }
        return render(request, 'pacientes/pages/page_create_paciente.html', data)
    else:
        return redirect('signin')


def tabela_pacientes(request):
    '''Tabela de pacientes'''
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
        return redirect('signin')


def delete_paciente(request, paciente_id):
    if request.user.is_authenticated:
        paciente = get_object_or_404(Paciente, pk = paciente_id)
        uuid_paciente = paciente.uuid_paciente

        if os.path.exists(os.path.join(settings.BASE_DIR, 'media', 'pacientes', uuid_paciente)):
            rmtree(os.path.join(settings.BASE_DIR, 'media', 'pacientes', uuid_paciente))

        paciente.delete()

        print('Paciente deletado!!')
        messages.error(request, 'Atenção!! Paciente excluído!,error')
        return redirect('tabela_pacientes')
    else:
        return redirect('signin')


def edit_paciente(request, paciente_id):
    if request.user.is_authenticated:
        paciente = get_object_or_404(Paciente, pk = paciente_id)
        if request.method == 'POST':
            nome = request.POST['nome']
            sobrenome = request.POST['sobrenome']
            email = request.POST['email']
            data_nascimento =  datetime.strptime(request.POST['data_nascimento'], "%d/%m/%Y").strftime("%Y-%m-%d")
            phone = request.POST['phone']
            massa = request.POST['massa']
            estatura = request.POST['estatura']
            unidade = request.POST['unidade']
            responsavel = request.POST['responsavel']
            status = request.POST['status']
            genero = request.POST['genero']

            change = 0
            try:
                path_imagem = request.FILES['path_imagem']
                change = 1
            except:
                try:
                    path_imagem = request.POST['path_imagem_exists']
                    change = 2
                except:
                    path_imagem = ''

            if validate_fields([nome, sobrenome, email, data_nascimento,
                                phone, massa, estatura, unidade, responsavel,
                                status, genero], request):
                print('-'*30)
                print(nome, sobrenome, email, data_nascimento, phone, massa, estatura, unidade,
                      responsavel, status, genero)
                print('-'*30)

                paciente.nome = nome
                paciente.sobrenome = sobrenome
                paciente.email = email
                paciente.data_nascimento = data_nascimento
                paciente.telefone = phone
                paciente.massa_corporal = massa
                paciente.estatura = estatura
                paciente.unidade = Unidade.objects.get(cidade=unidade)
                paciente.responsavel = Responsavel.objects.get(nome=responsavel)
                paciente.status = status
                paciente.genero = genero

                path_paciente = os.path.join(settings.BASE_DIR, 'media', 'pacientes', paciente.uuid_paciente)
                path_imagem = os.path.join(settings.BASE_DIR, 'media', 'pacientes', paciente.uuid_paciente, 'image.png')
                if change == 0:
                    if os.path.exists(path_imagem):
                        os.remove(path_imagem)
                    paciente.path_imagem = ''
                elif change == 1:
                    if os.path.exists(path_imagem):
                        os.remove(path_imagem)
                    arquivo_imagem = request.FILES['path_imagem']
                    fs = FileSystemStorage()
                    f = fs.save(os.path.join(path_paciente, 'image.png'), arquivo_imagem)
                    path_imagem = os.path.join(path_paciente, 'image.png')
                    paciente.path_imagem = path_imagem

                paciente.save()
                messages.success(request, 'SUCESSO!! Paciente editado!,success')

                return redirect('tabela_pacientes')

        else:
            data = {
                'paciente': paciente,
                'unidades': Unidade.objects.all(),
                'responsaveis': Responsavel.objects.all()
            }
            return render(request, 'pacientes/pages/page_edit_paciente.html', data)
    else:
        return redirect('signin')


def create_folder(uuid_paciente):
    path_pacientes = os.path.join(settings.BASE_DIR, 'media', 'pacientes')
    if not(os.path.exists(path_pacientes)):
        os.mkdir(path_pacientes)
    path_paciente = os.path.join(path_pacientes, uuid_paciente)
    if not(os.path.exists(path_paciente)):
        os.mkdir(path_paciente)
    return path_paciente