from django.contrib import admin
from .models import *

admin.site.register(Turno)
admin.site.register(Tipo_avaliacao)
admin.site.register(Ocorrencia)
admin.site.register(Manter_disciplinas)
admin.site.register(Estudante)
admin.site.register(Matricula)
admin.site.register(Turma)


class pessoaaInline(admin.TabularInline):
    model = pessoaa
    extra = 1


class Ocupacao_pessoaAdmin(admin.ModelAdmin):
    inlines = [pessoaaInline]

admin.site.register(pessoaa)
admin.site.register(Ocupacao_pessoa, Ocupacao_pessoaAdmin)

# class TurmaAdmin(admin.ModelAdmin):
#      inlines = [pessoaaInline]
# admin.site.register(Turma, TurmaAdmin)

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

admin.site.register(Curso)

class InstituicaoAdmin(admin.ModelAdmin):
    inlines = [CursoInline]

admin.site.register(Instituicao, InstituicaoAdmin)


class Area_do_saberAdmin(admin.ModelAdmin):
    inlines = [CursoInline]

admin.site.register(Area_do_saber, Area_do_saberAdmin)

class AvaliacaoInline(admin.TabularInline):
     model = Avaliacao
     extra = 1
admin.site.register(Avaliacao)

class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline]

admin.site.register(Disciplina, DisciplinaAdmin)


class CidadeInline(admin.TabularInline):
     model = Cidade
     extra = 1
admin.site.register(Cidade)
class FrequenciaInline(admin.TabularInline):
     model = Frequencia
     extra = 1
admin.site.register(Frequencia)
class ufAdmin(admin.ModelAdmin):
     inlines = [CidadeInline]

admin.site.register(uf, ufAdmin)


# class EstudanteAdmin(admin.ModelAdmin):
#      inlines = [AvaliacaoInline]

# admin.site.register(Estudante, EstudanteAdmin)

# class EstudanteAdmin(admin.ModelAdmin):
#      inlines = [FrequenciaInline]

# admin.site.register(Estudante, EstudanteAdmin)

# class DisciplinaAdmin(admin.ModelAdmin):
#     inlines = [AvaliacaoInline]
# admin.site.register(DisciplinaAdmin)
