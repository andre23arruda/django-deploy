import cv2
import os, c3d
import numpy as np
import os
from shutil import rmtree


def video_converter(arquivo, path_paciente):
    cap = cv2.VideoCapture(arquivo)
    success, image = cap.read()
    gray =  cv2.cvtColor(image,  cv2.COLOR_BGR2GRAY)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    output_name = 'output.mp4'
    path_output = os.path.join(path_paciente, output_name)

    out = cv2.VideoWriter(path_output, -1, fps, (gray.shape[1], gray.shape[0]))

    while success:
        out.write(image)

        success, image = cap.read()

    cap.release()
    out.release()

    return path_output


def get_c3d(path_c3d):
    event = {'labels': [], 'descriptions': [], 'contexts': [], 'times': None}

    try:
        with open(path_c3d, 'rb') as handle:
            reader = c3d.Reader(handle)
            groups = ((k, v) for k, v in reader.groups.items() if isinstance(k, str))
            for key, g in sorted(groups):
                if not isinstance(key, int):
                    for key, p in sorted(g.params.items()):
                        if len(p.dimensions) == 2:
                            C, R = p.dimensions
                            for r in range(R):
                                value = str(p.bytes[r * C:(r+1) * C])
                                value = value.replace("b'","")
                                value = value.replace("'","")
                                value = value.strip()
                                if g.name == 'EVENT' and p.name == 'DESCRIPTIONS':
                                    event['descriptions'].append(value)
                                elif g.name == 'EVENT' and p.name == 'CONTEXTS':
                                    event['contexts'].append(value)
                                elif g.name == 'EVENT' and p.name == 'LABELS':
                                    event['labels'].append(value)
                                elif g.name == 'EVENT' and p.name == 'TIMES':
                                    times = p.float_array
        times_1 = times[0, :]
        times_1 = times_1[np.nonzero(times_1)]

        times_2 = times[1, :]
        times_2 = times_2[np.nonzero(times_2)]

        event['times'] = np.hstack((times_1, times_2))

        return event

    except:
        raise Exception('Deu ruim!!')


def get_frames(path_video):
    cap = cv2.VideoCapture(path_video)
    success,image = cap.read()

    fps = cap.get(cv2.CAP_PROP_FPS)
    time_frame = 1 / fps

    count = 0
    times_frame = []

    video_frames = []

    while success:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        video_frames.append(gray)

        times_frame.append(time_frame * count)
        count += 1

        success,image = cap.read()

    times_frame = np.asarray(times_frame)

    return times_frame, video_frames


def event_frames(path_c3d, path_video, tempo):
    event = get_c3d(path_c3d)
    times_frame, video_frames = get_frames(path_video)

    times = event['times']
    sides = event['contexts']
    labels_list = event['labels']
    labels = [('Strike' in label) for label in labels_list]

    # Subtrai pelo tempo inicial do observador
    ERRO = 0
    TIME_START = tempo + ERRO
    TIME_END = TIME_START + 5
    times_bool = (times > TIME_START) & (times < TIME_END)
    times_new = times[times_bool]
    times_new = times_new - TIME_START
    times_new = times_new*2 # comente essa linha se for velocidade normal

    sides_new = np.asarray(sides)[times_bool]
    labels_new = np.asarray(labels_list)[times_bool]

    # Encontra os frames que estão no intervalo do erro
    ERRO = 0.02
    times_cicle = times_new[4:10]
    times_f = [np.where((times_frame >= tc - ERRO) & (times_frame <= tc + ERRO)) for tc in times_cicle]

    times_find = times_f[0:-2]
    times_find.append([[int(0.5 * (times_find[0][0][0] + times_find[2][0][0]))]])
    times_find.append([[int(0.5 * (times_f[3][0][0] + times_f[5][0][0]))]])

    # Salva os frames que temos interesse
    path_paciente = os.path.split(path_video)[0]
    path_imagem = os.path.join(path_paciente, 'frames')

    if os.path.exists(path_imagem):
        rmtree(path_imagem)
    os.mkdir(path_imagem)

    name_imagem = os.path.splitext(os.path.split(path_video)[1])[0]
    path_imagem = os.path.join(path_imagem, name_imagem)

    position = (430,100) # posição do texto na imagem
    thickness = 2 # grossura da fonte

    path_frames = {}
    for i, tf in enumerate(times_find):
        print('Frame: ', tf[0])
        image = video_frames[tf[0][0]]

        # coloca texto na imagem
        cv2.putText(image, f'{sides_new[i]} {labels_new[i]}',
                    position, cv2.FONT_HERSHEY_PLAIN, 2,
                    (209, 80, 0, 255), 2)

        # salva imagem
        cv2.imwrite(path_imagem + f'_frame_{str(tf[0][0])}.png',  image)
        path_frames[i] = path_imagem + f'_frame_{str(tf[0][0])}.png'
    return path_frames