from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage

from cadastro_pessoa.models import Cliente, Paciente, Responsavel, Unidade
import os
from shutil import rmtree
from ..src.utils import video_converter, event_frames

def teste(request, paciente_id):

    data = {'path_frames': None, 'path_video': None}

    if request.method == 'POST':
        paciente = get_object_or_404(Paciente, pk = paciente_id)

        try:
            video = request.FILES['path_video']
            c3d_file = request.FILES['path_c3d']
            tempo = float(request.POST['tempo'])
            print(video, c3d_file, tempo, type(tempo))

            path_paciente = os.path.join(settings.BASE_DIR, 'media', 'pacientes', paciente.uuid_paciente)
            path_video = os.path.join(settings.BASE_DIR, 'media', 'pacientes', paciente.uuid_paciente, video.name)
            path_c3d = os.path.join(settings.BASE_DIR, 'media', 'pacientes', paciente.uuid_paciente, c3d_file.name)

            print(path_video)

            # fs = FileSystemStorage()
            # f = fs.save(path_video, video)

            # fs = FileSystemStorage()
            # if os.path.exists(path_c3d):
            #     rmtree(path_c3d)
            # f = fs.save(path_c3d, c3d_file)

            # path_output = video_converter(path_video, path_paciente)
            # os.remove(path_video)

            path_frames = None
            # path_frames = event_frames(path_c3d, path_output, tempo)
            path_output = os.path.join(settings.BASE_DIR, 'media', 'pacientes', paciente.uuid_paciente, 'output.mp4')

            data = {'path_frames': path_frames, 'path_video': path_output}

        except:
            pass

    return render(request, 'teste.html', data)