# Generated by Django 4.1.3 on 2022-11-12 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUber', '0022_alter_servicos_servicos_alter_servicos_veiculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicos',
            name='veiculo',
            field=models.IntegerField(choices=[(1, 'Moto'), (2, 'carro'), (3, 'caminhão'), (4, 'carreta')], verbose_name='veículo'),
        ),
    ]
