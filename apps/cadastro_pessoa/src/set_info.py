import json
from ..models import Paciente


def set_protocolos(paciente, novo_protocolo):
    text = paciente.protocolos
    protocolos = json.loads(text)
    protocolos.extend(novo_protocolo)
    protocolos = json.dumps(sorted(list(set(protocolos)))) # remove duplicados
    return protocolos


def get_protocolos(paciente):
    text = paciente.protocolos
    protocolos = json.loads(text)
    return protocolos


def count_status(pacientes, status):

    def get_status(paciente):
        if paciente.status.upper() == status.upper():
            return True

    number_status = len(list(filter(get_status, pacientes)))
    return number_status
