# Generated by Django 3.0.7 on 2020-06-25 13:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=20)),
                ('primeiro_nome', models.CharField(max_length=20)),
                ('sobrenome', models.CharField(max_length=20)),
                ('data_nascimento', models.DateField(blank=True)),
                ('telefone', models.CharField(max_length=20)),
                ('data_cadastro', models.DateField(blank=False, auto_now_add=True)),
            ],
        ),
    ]
