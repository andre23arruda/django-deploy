from django.shortcuts import render, redirect
from django.conf import settings

from . import src


def resultado_signin(request):
   ''' Página de autenticação para o cliente visualizar resultado '''
   if request.method == 'POST':
      result = src.recaptcha(request)
      if result['success']:
         return redirect('resultado_table')
   return render(request, 'resultados/pages/page_signin.html', {'site_key': settings.RECAPTCHA_SITE_KEY})


def resultado_table(request):
   return render(request, 'resultados/pages/page_table.html')


def teste(request):
   return render(request, 'teste.html')
