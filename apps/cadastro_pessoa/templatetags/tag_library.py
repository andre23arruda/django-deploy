from django.shortcuts import get_object_or_404
from django import template
from datetime import datetime

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


@register.filter(name='get_responsavel')
def get_responsavel(paciente):
    return paciente.responsavel