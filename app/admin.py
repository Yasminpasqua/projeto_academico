from django.contrib import admin
from .models import *

admin.site.register(Disciplina)
admin.site.register(Cidade)
admin.site.register(Turma)
admin.site.register(Area_do_saber)
admin.site.register(Curso)
admin.site.register(Turno)
admin.site.register(Tipo_avaliacao)
admin.site.register(Ocorrencia)
admin.site.register(Instituicao)
admin.site.register(Manter_disciplinas)
admin.site.register(Frequencia)
admin.site.register(Avaliacao)

class pessoaaInline(admin.TabularInline):
    model = pessoaa
    extra = 1 

class Ocupacao_pessoaAdmin(admin.ModelAdmin):

    inlines = [pessoaaInline]

admin.site.register(pessoaa)
admin.site.register(Ocupacao_pessoa, Ocupacao_pessoaAdmin)



