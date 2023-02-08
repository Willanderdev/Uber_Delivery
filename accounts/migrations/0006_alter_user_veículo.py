# Generated by Django 4.1.3 on 2023-02-06 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_veículo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='veículo',
            field=models.CharField(choices=[('moto', 'moto'), ('carro', 'carro'), ('caminhão', 'caminhão'), ('carreta', 'carreta')], default='', max_length=20, verbose_name='veículo'),
        ),
    ]
