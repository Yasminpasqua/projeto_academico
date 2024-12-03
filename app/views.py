from django.shortcuts import render
from django.views import View
from .models import *
def index(request):
    return render(request, 'index.html')
class FrequenciaView(View):
    def get(self, request, *args, **kwargs):
        frequencias = Frequencia.objects.all()
        return render(request, 'frequencia.html', {'frequencias': frequencias})

# class LivrosView(View):
#     def get(self, request, *args, **kwargs):
#         livros = Livro.objects.all()
#         return render(request, 'livros.html', {'livros': livros})