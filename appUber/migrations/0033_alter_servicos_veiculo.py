# Generated by Django 4.1.3 on 2022-11-13 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUber', '0032_alter_servicos_distancia_alter_servicos_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicos',
            name='veiculo',
            field=models.IntegerField(blank=True, choices=[('moto', 'moto'), ('carro', 'carro'), ('caminhão', 'caminhão'), ('carreta', 'carreta')], verbose_name='veiculo'),
        ),
    ]
