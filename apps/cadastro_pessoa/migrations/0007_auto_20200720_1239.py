# Generated by Django 3.0.7 on 2020-07-20 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_pessoa', '0006_auto_20200720_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='path_imagem',
            field=models.TextField(),
        ),
    ]