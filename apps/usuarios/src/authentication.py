from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings

import json
import requests

def authentication_email(email, request):
    ''' Retorna username através do email de entrada '''
    if User.objects.filter(email=email).exists():
        username = User.objects.filter(email=email).values_list('username', flat = True).get()
        return username
    return None

def authentication_username(username, request):
    ''' Retorna username através do username de entrada '''
    if User.objects.filter(username=username).exists():
        username = User.objects.filter(username=username).values_list('username', flat = True).get()
        return username
    messages.error(request, 'ERRO!! Usuário não cadastrado!,error')
    return None


def recaptcha(request):
   recaptcha_response = request.POST.get('g-recaptcha-response')
   data = {
         'secret': settings.RECAPTCHA_SECRET_KEY,
         'response': recaptcha_response,
   }
   r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
   result = r.json()
   return result