# Generated by Django 5.1.3 on 2024-12-17 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_frequencia_estudante_frequencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequencia',
            name='numero_faltas',
            field=models.IntegerField(verbose_name='Numero de faltas'),
        ),
    ]