# Generated by Django 4.1.3 on 2022-11-12 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUber', '0021_alter_servicos_servicos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicos',
            name='servicos',
            field=models.IntegerField(choices=[(1, 'viagem'), (2, 'delivery')], verbose_name='servicos'),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='veiculo',
            field=models.IntegerField(blank=True, choices=[(1, 'Moto'), (2, 'carro'), (3, 'caminhão'), (4, 'carreta')], verbose_name='veículo'),
        ),
    ]
