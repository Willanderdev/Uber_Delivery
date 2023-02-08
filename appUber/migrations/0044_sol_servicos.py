# Generated by Django 4.1.3 on 2023-02-02 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUber', '0043_alter_servicos_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sol_Servicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicos', models.CharField(choices=[('viagem', 'viagem'), ('delivery', 'delivery')], max_length=10, verbose_name='servicos')),
                ('coleta', models.CharField(max_length=100, verbose_name='coleta')),
                ('entrega', models.CharField(max_length=100, verbose_name='entrega')),
                ('time', models.CharField(blank=True, max_length=20, verbose_name='time')),
                ('distancia', models.DecimalField(blank=True, decimal_places=2, max_digits=15, verbose_name='distancia')),
                ('veiculo', models.CharField(choices=[('moto', 'moto'), ('carro', 'carro'), ('caminhao', 'caminhão'), ('carreta', 'carreta')], max_length=10, verbose_name='veiculo')),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=15, verbose_name='valor')),
                ('status', models.CharField(blank=True, choices=[('Waiting', 'Waiting'), ('Pending', 'Pending'), ('Accepted', 'Accepted')], max_length=15, null=True, verbose_name='status')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
