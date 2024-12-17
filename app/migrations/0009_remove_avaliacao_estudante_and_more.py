# Generated by Django 5.1.3 on 2024-12-17 16:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_avaliacao_estudante_disciplina_estudante_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacao',
            name='estudante',
        ),
        migrations.RemoveField(
            model_name='disciplina',
            name='estudante',
        ),
        migrations.RemoveField(
            model_name='frequencia',
            name='estudante',
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='nota',
            field=models.IntegerField(verbose_name='Descricao'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tipo_avaliacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipo_avaliacao', verbose_name='Pessoa'),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='Frequencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.frequencia', verbose_name='frequencias'),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='avaliacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.avaliacao', verbose_name='Avaliacoes'),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina', verbose_name='Disciplina'),
        ),
        migrations.AlterField(
            model_name='frequencia',
            name='numero_faltas',
            field=models.IntegerField(verbose_name='Descricao'),
        ),
    ]