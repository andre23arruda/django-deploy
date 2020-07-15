from django.shortcuts import get_object_or_404
from django import template
from datetime import datetime
import json

register = template.Library()


@register.filter()
def age(value):
    return datetime.now().year - int(value.year)


@register.filter(name='lookup')
def lookup(pacientes, status):

    def get_status(paciente):
        if paciente.status.upper() == status.upper():
            return True

    number_status = len(list(filter(get_status, pacientes)))
    return number_status


@register.filter(name='percent')
def percent(value, arg):
    "Multiplies the arg and the value"
    return 100 * (int(value)/int(arg))


@register.filter(name='date2template')
def date2template(value):
    return value.strftime("%d/%m/%Y")


@register.filter(name='date_replace')
def date_replace(value):
    return value.replace("/",'_')


@register.filter(name='get_responsavel')
def get_responsavel(paciente):
    return paciente.responsavel


@register.filter(name='get_protocolos')
def get_protocolos(paciente):
    text = paciente.protocolos
    protocolos = json.loads(text)
    return protocolos


@register.filter(name='get_keys')
def get_keys(value):
    return list(value.keys())


@register.filter(name='get_index_value')
def get_index_value(value, element):
    return value[element]