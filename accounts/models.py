# coding=utf-8

import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    
    Tipo_de_user = (
          ('usuario', 'usuario'),
          ('colaborador', 'colaborador')
      )
    
    veículos = (
        ('moto', 'moto'),
        ('carro', 'carro'),
        ('caminhão', 'caminhão'),
        ('carreta', 'carreta')
    )

    username = models.CharField(
        'Apelido / Usuário', max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'Informe um nome de usuário válido. '
                'Este valor deve conter apenas letras, números '
                'e os caracteres: @/./+/-/_ .'
                , 'invalid'
            )
        ], help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma'
    )
    tipo = models.CharField(
        'tipo_de_usuario', choices=Tipo_de_user, max_length=20, default='usuario')
    veículo = models.CharField(
        'veículo', choices=veículos, max_length=20, default='')
    name = models.CharField('Nome', max_length=100, blank=True)
    email = models.EmailField('E-mail', unique=True)
    image = models.ImageField(
        'image', upload_to='user', blank=True, null=True)
    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]
    
    def to_dict(self):
        return{
            'username': self.username,
            'name': self.name,
            'email': self.email
        }
