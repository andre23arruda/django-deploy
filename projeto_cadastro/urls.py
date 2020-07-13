from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from django.conf.urls import handler404, handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/password_reset/', views.PasswordResetView.as_view(
        html_email_template_name='registration/password_reset_email.html')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('cadastro_pessoa.urls')),
    path('pacientes/', include('cadastro_pessoa.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('resultados/', include('resultados.urls'))
]

handler404 = 'cadastro_pessoa.views.error_404_view'
