# Generated by Django 4.1.3 on 2023-02-02 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tipo',
            field=models.CharField(choices=[('usuario', 'usuario'), ('colaborador', 'colaborador')], default='usuario', max_length=20, verbose_name='tipo_de_usuario'),
        ),
    ]
