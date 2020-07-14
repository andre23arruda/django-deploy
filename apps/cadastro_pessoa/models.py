from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User


# generos para escolha no cadastro
GENDER = (('M', 'Masculino'),('F', 'Feminino'))

# lista de status de protocolos
STATUS = (
    ("Aberto", "Aberto"),
    ("Em andamento", "Em andamento"),
    ("Finalizado", "Finalizado")
)

# lista de estados para escolher no cadastro
ESTADOS = [('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'),
           ('BA', 'BA'), ('CE', 'CE'), ('ES', 'ES'), ('GO', 'GO'),
           ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'),
           ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'),
           ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'),
           ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'),
           ('SE', 'SE'), ('TO', 'TO')]


class Responsavel(models.Model):
    '''Resposavel cadastrado'''
    nome = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.nome


class Unidade(models.Model):
    '''Unidade cadastrada'''
    cidade = models.CharField(max_length=40, null=False, blank=False)
    estado = models.CharField(max_length=2, choices=ESTADOS)

    def __str__(self):
        return f'{self.cidade}-{self.estado}'


class Cliente(models.Model):
    usuario = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    primeiro_nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    data_nascimento = models.DateField(blank=True)
    telefone = models.CharField(max_length=20)
    data_cadastro = models.DateField(blank=False, auto_now_add=True)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Cliente._meta.fields]


class Paciente(models.Model):
    '''Cadastro de paciente'''
    nome = models.CharField(max_length=20, null=False, blank=False)
    sobrenome = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    data_nascimento = models.DateField(blank=False)
    data_cadastro = models.DateField(blank=False)
    telefone = models.CharField(max_length=20)
    massa_corporal = models.IntegerField()
    estatura = models.IntegerField()
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS)
    genero = models.CharField(max_length=1, choices=GENDER)
    protocolos = models.TextField(default='[]')
    path_imagem = models.ImageField(upload_to=f'images/{datetime.now().strftime("%m/%d/%Y")}', blank=True)

    def __str__(self):
        return  f'{self.nome} {self.sobrenome}'

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Paciente._meta.fields]
