# from django.db import models

# from django.contrib.auth import get_user_model


# VEICULO = [
#     ('moto', 'moto'),
#     ('carro', 'carro'),
#     ('caminhao', 'caminhão'),
#     ('carreta', 'carreta')
# ]

# class Colaborador(models.Model):
#     # full_name = models.ForeignKey(get_user_model(), verbose_name='nome', on_delete=models.CASCADE)
#     nome_sobrenome = models.CharField('nome', max_length=100)
#     cpf = models.CharField('cpf', max_length=15)
#     categoria = models.CharField('veiculo', max_length=10, choices=VEICULO)
#     is_staff = models.BooleanField('Membro da equipe', default=True)
    
#     def __str__(self):
#         return self.full_name

