# Generated by Django 4.1.3 on 2022-11-20 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUber', '0038_servicos_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicos',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('accepted', 'accepted')], max_length=15, verbose_name='status'),
        ),
    ]
