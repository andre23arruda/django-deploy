# Generated by Django 3.0.7 on 2020-07-21 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_pessoa', '0007_auto_20200720_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='massa_corporal',
            field=models.FloatField(),
        ),
    ]
