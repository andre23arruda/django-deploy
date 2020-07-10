from django.contrib.auth.models import User

def authentication_email(email):
    ''' Retorna username através do email de entrada '''
    if User.objects.filter(email=email).exists():
        username = User.objects.filter(email=email).values_list('username', flat = True).get()
        return username
    return None

def authentication_username(username):
    ''' Retorna username através do username de entrada '''
    if User.objects.filter(username=username).exists():
        username = User.objects.filter(username=username).values_list('username', flat = True).get()
        return username
    return None