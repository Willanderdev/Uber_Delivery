from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify

VEICULO = [
    ('moto', 'moto'),
    ('carro', 'carro'),
    ('caminhao', 'caminhão'),
    ('carreta', 'carreta')
]

SERVICOS = [('viagem', 'viagem'),
            ('delivery', 'delivery')
            ]

STATUS = [
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted')
]

class Servicos(models.Model):
    servicos = models.CharField('servicos', max_length=10, choices=SERVICOS)
    coleta = models.CharField('coleta', max_length=100)
    entrega = models.CharField('entrega', max_length=100)
    time = models.CharField('time', blank=True, max_length=20)
    distancia = models.DecimalField('distancia', blank=True, max_digits=15, decimal_places=2)
    veiculo = models.CharField('veiculo', max_length=10, choices=VEICULO)
    valor = models.DecimalField('valor', blank=True, max_digits=15, decimal_places=2)
    status = models.CharField('status', max_length=15,
                              blank=True, choices=STATUS)

    class Meta:
        ordering = ['id']

    def __str__(self):
        
        return self.servicos