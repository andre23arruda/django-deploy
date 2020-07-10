from django.contrib import admin
from .models import Cliente, Paciente, Unidade, Responsavel


class ListaPaciente(admin.ModelAdmin):
    list_display = ('id', 'email', 'nome', 'sobrenome', 'data_nascimento')
    list_display_links = ('id', 'email')
    search_fields = ('nome',)
    list_filter = ('status',)
    list_per_page = 10
    ordering = ('id',)


class ListaUnidade(admin.ModelAdmin):
    list_display = ('cidade', 'estado')
    list_display_links = ('cidade',)
    search_fields = ('cidade',)
    list_filter = ('estado',)
    list_per_page = 10
    ordering = ('cidade',)


class ListaResponsavel(admin.ModelAdmin):
    list_display = ('nome',)
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page = 10
    ordering = ('nome',)


admin.site.register(Paciente, ListaPaciente)
admin.site.register(Unidade, ListaUnidade)
admin.site.register(Responsavel, ListaResponsavel)