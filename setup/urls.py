from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views
from django.conf.urls import handler404, handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/password_reset/',
         views.PasswordResetView.as_view(html_email_template_name='registration/password_reset_email.html')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('pacientes/', include('cadastro_pessoa.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('resultados/', include('resultados.urls')),
    path('', include('dashboard.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'cadastro_pessoa.views.error_404_view'