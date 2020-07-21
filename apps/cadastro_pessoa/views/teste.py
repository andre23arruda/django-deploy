from django.shortcuts import get_object_or_404

from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from django.http import FileResponse
from cadastro_pessoa.models import Paciente, Responsavel, Unidade

import os, uuid, io
from datetime import datetime

def teste(request, paciente_id):

    paciente = get_object_or_404(Paciente, pk = paciente_id)

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)
    doc.title = f'report_{paciente.uuid_paciente}'
    Story=[]
    logo = paciente.path_imagem
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    im = Image(logo, 2*inch, 2*inch)
    im.hAlign = 'LEFT'
    Story.append(im)
    Story.append(Spacer(1, 12))

    ptext = f'<font size="12">UUID: { paciente.uuid_paciente }</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = f'<font size="12">Paciente: { paciente }</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = f'<font size="12">Data de nascimento: { paciente.data_nascimento.strftime("%d/%m/%Y") }</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = f'<font size="12">Gênero: { paciente.genero }</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = f'<font size="12">Altura: { paciente.estatura }cm</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = f'<font size="12">Massa corporal: { paciente.massa_corporal }kg</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = f'<font size="12">Reponsável: { paciente.responsavel.nome }</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = f'<font size="12">Unidade: { paciente.unidade }</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = f'<font size="12">Status: { paciente.status }</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 48))

    ptext = '<font size="12">Harpia Health Solutions</font>'
    ptext_style = styles['Heading1']
    ptext_style.alignment = 1
    Story.append(Paragraph(ptext, ptext_style))
    Story.append(Spacer(1, 12))
    doc.build(Story)

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='report.pdf')