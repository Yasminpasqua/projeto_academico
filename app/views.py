from django.shortcuts import render
from django.views import View
from .models import *
def index(request):
    return render(request, 'index.html')
class FrequenciaView(View):
    def get(self, request, *args, **kwargs):
        frequencias = Frequencia.objects.all()
        return render(request, 'frequencia.html', {'frequencias': frequencias})

class CursoView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, 'curso.html', {'cursos': cursos})

class InstituicaoView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = Instituicao.objects.all()
        return render(request, 'instituicao.html', {'instituicoes': instituicoes})
class Area_do_saberView(View):
    def get(self, request, *args, **kwargs):
        areas_do_saber = Area_do_saber.objects.all()
        return render(request, 'area_do_saber.html', {'areas_do_saber': areas_do_saber})
class DisciplinaView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplina.objects.all()
        return render(request, 'disciplina.html', {'disciplinas': disciplinas})
class Ocupacao_pessoaView(View):
    def get(self, request, *args, **kwargs):
        ocupacao_pessoas = Ocupacao_pessoa.objects.all()
        return render(request, 'ocupacao_pessoa.html', {'ocupacao_pessoas': ocupacao_pessoas})
class PessoaaView(View):
    def get(self, request, *args, **kwargs):
        pessoas = pessoaa.objects.all()
        return render(request, 'pessoaa.html', {'pessoas': pessoas})
class TurnoView(View):
    def get(self, request, *args, **kwargs):
        turnos = Turno.objects.all()
        return render(request, 'turno.html', {'turnos': turnos})
class Tipo_avaliacaoView(View):
    def get(self, request, *args, **kwargs):
        tipos_avaliacoes = Tipo_avaliacao.objects.all()
        return render(request, 'tipo_avaliacao.html', {'tipos_avaliacoes': tipos_avaliacoes})
class OcorrenciaView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'ocorrencia.html', {'ocorrencias': ocorrencias})
class Manter_disciplinasView(View):
    def get(self, request, *args, **kwargs):
        manter_disciplinas = Manter_disciplinas.objects.all()
        return render(request, 'manter_disciplinas.html', {'manter_disciplinas': manter_disciplinas})
class TurmaView(View):
    def get(self, request, *args, **kwargs):
        turmas = Turma.objects.all()
        return render(request, 'turma.html', {'turmas': turmas})
class CidadeView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})
class AvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacao.html', {'avaliacoes': avaliacoes})
class MatriculaView(View):
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.all()
        return render(request, 'matricula.html', {'matriculas': matriculas})