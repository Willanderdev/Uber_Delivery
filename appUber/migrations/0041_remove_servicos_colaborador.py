# Generated by Django 4.1.3 on 2022-11-22 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appUber', '0040_servicos_colaborador_alter_servicos_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicos',
            name='colaborador',
        ),
    ]
