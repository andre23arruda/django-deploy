from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from cadastro_pessoa.models import Cliente, Paciente, Responsavel, Unidade
from datetime import datetime
from django.contrib import messages
from django.conf import settings

import os


def dicom_viewer(request):
    if request.user.is_authenticated:
        return render(request, 'pages/viewer.html')
    else:
        return redirect('../usuarios/signin')