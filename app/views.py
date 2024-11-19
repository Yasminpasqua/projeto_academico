from django.shortcuts import render
from django.views import View
from .models import *
def index(request):
    return render(request, 'app/index.html')