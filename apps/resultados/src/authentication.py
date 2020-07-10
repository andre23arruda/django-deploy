from django.conf import settings
import json
import requests

def recaptcha(request):
   recaptcha_response = request.POST.get('g-recaptcha-response')
   data = {
         'secret': settings.RECAPTCHA_SECRET_KEY,
         'response': recaptcha_response,
   }
   r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
   result = r.json()
   return result