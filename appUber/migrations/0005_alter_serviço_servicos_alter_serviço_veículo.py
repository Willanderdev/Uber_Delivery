# Generated by Django 4.1.3 on 2022-11-08 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUber', '0004_serviço_servicos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviço',
            name='servicos',
            field=models.IntegerField(choices=[(1, 'viagem'), (2, 'delivery')], null=True),
        ),
        migrations.AlterField(
            model_name='serviço',
            name='veículo',
            field=models.IntegerField(choices=[(1, 'Moto'), (2, 'carro'), (3, 'caminhão'), (4, 'carreta')]),
        ),
    ]
