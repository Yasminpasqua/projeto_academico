# Create your models here.
from django.db import models 


class Cidade(models.Model):
        nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
        uf = models.CharField(max_length=2, verbose_name="UF")
        def __str__(self):
            return f"{self.nome}, {self.uf}"
        class Meta:
            verbose_name = "Cidade"
            verbose_name_plural = "Cidades"

class Turma(models.Model):
        nome = models.CharField(max_length=100, verbose_name="Nome da turma")
        turno = models.CharField(max_length=100, verbose_name="Turno")
        def __str__(self):
            return self.nome
        class Meta:
            verbose_name = "Turma"
            verbose_name_plural = "Turmas"

class Ocupacao_pessoa(models.Model):
        nome = models.CharField(max_length=100, verbose_name="Nome")
        def __str__(self):
            return self.nome
        class Meta:
            verbose_name = "Ocupacao_pessoa"
            verbose_name_plural = "Ocupacao_pessoas"

class Area_do_saber(models.Model):
        nome = models.CharField(max_length=100, verbose_name="Nome")
        def __str__(self):
            return self.nome
        class Meta:
            verbose_name = "Area_do_saber"
            verbose_name_plural = "Areas_do_saber"

class Curso(models.Model):
        nome = models.CharField(max_length=100, verbose_name="Nome do curso")
        duracao_meses= models.CharField(max_length=100, unique=True,verbose_name="Duracao_meses")
        carga_horaria_total= models.IntegerField(verbose_name="Carga horaria total")
        area_saber = models.ForeignKey('Area_do_saber', on_delete=models.CASCADE, verbose_name="Area do saber")
        instituicao = models.ForeignKey('Instituicao', on_delete=models.CASCADE, verbose_name="Instituicao")
        def __str__(self):
            return self.nome
        class Meta:
            verbose_name = "Curso"
            verbose_name_plural = "Cursos"

class Turno(models.Model):
        nome = models.CharField(max_length=100, verbose_name="Nome do turno")
        def __str__(self):
            return self.nome
        class Meta:
            verbose_name = "Turno"
            verbose_name_plural = "Turnos"
          
class Disciplina(models.Model):
        nome = models.CharField(max_length=100, verbose_name="Nome da disciplina")
        area_saber = models.ForeignKey('Area_do_saber', on_delete=models.CASCADE, verbose_name="Area do saber")
        def __str__(self):
            return self.nome
        class Meta:
            verbose_name = "Disciplina"
            verbose_name_plural = "Disciplinas"

class Tipo_avaliacao(models.Model):
        nome = models.CharField(max_length=100, verbose_name="Tipo da avaliacao")
        def __str__(self):
            return self.nome
        class Meta:
            verbose_name = "Tipo_avaliacao"
            verbose_name_plural = "Tipos_avaliacoes"

class Ocorrencia(models.Model):
        descricao = models.CharField(max_length=100, verbose_name="Descricao")
        data= models.DateField(verbose_name="Data")
        curso = models.ForeignKey('Curso', on_delete=models.CASCADE, verbose_name="Curso")
        disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE, verbose_name="Disciplina")
        pessoa = models.ForeignKey('pessoaa', on_delete=models.CASCADE, verbose_name="Pessoa")
        def __str__(self):
            return self.nome
        class Meta:
            verbose_name = "Ocorrencia"
            verbose_name_plural = "Ocorrencias"



        # Superclasse de 'pessoa' que sera uma classe pai para: pessoafísica e pessoajurídica

class Pessoa(models.Model):
        nome= models.CharField(max_length=255, default='')
        cidade= models.ForeignKey('Cidade', on_delete=models.CASCADE, default=1)

        class Meta:
            abstract = True

        def __str__(self):
            return self.nome

class pessoaFisica(Pessoa):
        cpf = models.CharField(max_length=255, default='')
        data_nasc = models.DateField(default='2000-01-01')
        email= models.CharField(max_length=255, default='')
        nome_do_pai= models.CharField(max_length=255, default='')
        nome_da_mae= models.CharField(max_length=255, default='')
        ocupacao= models.ForeignKey('Ocupacao_pessoa', on_delete=models.CASCADE, default=1)

        class Meta:
            abstract=True

class pessoaJurídica(Pessoa):
        site= models.CharField(max_length=255, default='')
        telefone = models.CharField(max_length=255, default='')

        class Meta:
            abstract=True



class Instituicao(pessoaJurídica):
        pass

        class Meta:
            verbose_name='Instituicao'
            verbose_name_plural='Instituicoes' 

class pessoaa(pessoaFisica):
        pass

        class Meta:
            verbose_name='pessoa'
            verbose_name_plural='pessoas' 


class Manter_disciplinas(models.Model):
        carga_horaria = models.IntegerField(verbose_name="Descricao")
        curso = models.ForeignKey('Curso', on_delete=models.CASCADE, verbose_name="Curso")
        disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE, verbose_name="Disciplina")
        pessoa = models.ForeignKey('pessoaa', on_delete=models.CASCADE, verbose_name="Pessoa")
        def __str__(self):
            return self.nome
        class Meta:
            verbose_name = "Manter_disciplina"
            verbose_name_plural = "Manter_disciplinas"

class Frequencia(models.Model):
        numero_faltas = models.IntegerField(verbose_name="Descricao")
        curso = models.ForeignKey('Curso', on_delete=models.CASCADE, verbose_name="Curso")
        disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE, verbose_name="Disciplina")
        pessoa = models.ForeignKey('pessoaa', on_delete=models.CASCADE, verbose_name="Pessoa")
        class Meta:
            abstract=True
        def __str__(self):
            return self.nome
        class Meta:
            verbose_name = "Frequencia"
            verbose_name_plural = "Frequencias"

class Avaliacao(models.Model):
        descricao= models.CharField(max_length=255, default='')
        nota = models.IntegerField(verbose_name="Descricao")
        curso = models.ForeignKey('Curso', on_delete=models.CASCADE, verbose_name="Curso")
        disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE, verbose_name="Disciplina")
        tipo_avaliacao = models.ForeignKey('Tipo_avaliacao', on_delete=models.CASCADE, verbose_name="Pessoa")
        def __str__(self):
            return self.nome
        class Meta:
            verbose_name = "Avaliacao"
            verbose_name_plural = "Avaliacoes"