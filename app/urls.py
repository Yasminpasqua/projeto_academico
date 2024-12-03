from django.urls import path
from .views import *
from django.urls import path,include
from .import views 

urlpatterns = [
    path('', views.index, name='index'),  # Certifique-se de que views.index exista
    path('frequencia/', FrequenciaView.as_view(), name='frequencia'),  # Corrigido o nome da URL para minúsculo
]