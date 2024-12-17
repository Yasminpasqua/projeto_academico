from django.urls import path
from .views import *
from django.urls import path,include
from .import views 

urlpatterns = [
    path('', views.index, name='index'),  # Certifique-se de que views.index exista
    path('frequencia/', FrequenciaView.as_view(), name='frequencia'),  # Corrigido o nome da URL para minúsculo
    path('curso/', CursoView.as_view(), name='curso'),
    path('instituicao/', InstituicaoView.as_view(), name='instituicao'),
    path('area_do_saber/', Area_do_saberView.as_view(), name='area_do_saber'),
    path('disciplina/', DisciplinaView.as_view(), name='disciplina'),
    path('ocupacao_pessoa/', Ocupacao_pessoaView.as_view(), name='ocupacao_pessoa'),
    path('pessoaa/', PessoaaView.as_view(), name='pessoaa'),
    path('turno/', TurnoView.as_view(), name='turno'),
    path('tipo_avaliacao/', Tipo_avaliacaoView.as_view(), name='tipo_avaliacao'),
    path('ocorrencia/', OcorrenciaView.as_view(), name='ocorrencia'),
    path('manter_disciplinas/', Manter_disciplinasView.as_view(), name='manter_disciplina'),
    path('turma/', TurmaView.as_view(), name='turma'),
    path('cidade/', CidadeView.as_view(), name='cidade'),
    path('avaliacao/', AvaliacaoView.as_view(), name='avaliacao'),
    path('matricula/', MatriculaView.as_view(), name='matricula'),
]