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

##################### Para usar no futuro #####################
# def get_protocolos(paciente):
#     path_file = paciente.protocolos
#     with open(path_file) as json_file:
#         protocolos = json.load(json_file)
#     return protocolos


# def save_protocolos(paciente, protocolos):
#     with open(paciente.protocolos, 'w') as json_file:
#         json.dump(protocolos, json_file)

# def set_protocolos(paciente, novo_protocolo):
#     hoje = datetime.now().strftime("%d/%m/%Y")
#     protocolos = get_protocolos(paciente)
#     protocolos[hoje] = {novo:'' for novo in novo_protocolo}
#     save_protocolos(paciente, protocolos)


# def set_data_protocolos(request, paciente, data_exame):
#     protocolos = get_protocolos(paciente)
#     data_exame_replace = data_exame.replace('_', '/')
#     protocolos_exame = protocolos[data_exame_replace]

#     for protocolo in protocolos_exame.keys():
#         protocolos[data_exame_replace][protocolo] = request.POST.getlist(data_exame + '_' + protocolo)

#     save_protocolos(paciente, protocolos)