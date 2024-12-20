# Generated by Django 5.1.3 on 2024-12-03 19:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_cidade_uf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=255)),
                ('cpf', models.CharField(default='', max_length=255)),
                ('data_nasc', models.DateField(default='2000-01-01')),
                ('email', models.CharField(default='', max_length=255)),
                ('nome_do_pai', models.CharField(default='', max_length=255)),
                ('nome_da_mae', models.CharField(default='', max_length=255)),
                ('avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.avaliacao', verbose_name='Avaliacoes')),
                ('cidade', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.cidade')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina', verbose_name='Disciplina')),
                ('frequencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.frequencia', verbose_name='frequencias')),
                ('ocupacao', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.ocupacao_pessoa')),
            ],
            options={
                'verbose_name': 'estudante',
                'verbose_name_plural': 'estudantes',
            },
        ),
    ]
