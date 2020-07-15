import json
from datetime import datetime

from ..models import Paciente


def set_protocolos(paciente, novo_protocolo):
    hoje = datetime.now().strftime("%d/%m/%Y")
    text = paciente.protocolos
    protocolos = json.loads(text)
    protocolos[hoje] = {novo:'' for novo in novo_protocolo}
    protocolos = json.dumps(protocolos) # remove duplicados
    return protocolos


def get_protocolos(paciente):
    text = paciente.protocolos
    protocolos = json.loads(text)
    return protocolos
