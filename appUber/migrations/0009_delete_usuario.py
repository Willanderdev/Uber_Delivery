# Generated by Django 4.1.3 on 2022-11-08 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appUber', '0008_alter_serviço_coleta_alter_serviço_entrega_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]