# Generated by Django 4.1.3 on 2022-11-20 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUber', '0036_alter_servicos_options_servicos_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicos',
            name='servicos',
            field=models.CharField(choices=[('viagem', 'viagem'), ('delivery', 'delivery')], max_length=10, verbose_name='servicos'),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='veiculo',
            field=models.CharField(choices=[('moto', 'moto'), ('carro', 'carro'), ('caminhao', 'caminhão'), ('carreta', 'carreta')], max_length=10, verbose_name='veiculo'),
        ),
    ]