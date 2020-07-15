from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from cadastro_pessoa.models import Cliente, Paciente, Responsavel, Unidade
from datetime import datetime
from django.contrib import messages
from django.conf import settings

import os


def error_404_view(request, exception):
    return render(request,'error/404.html')


def error_500_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'error/500.html', data)