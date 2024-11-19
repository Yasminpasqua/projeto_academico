from django.urls import path
from .views import *
from django.urls import path,include
from .import views 

urlpatterns = [
    path('', views.index, name='index'),
]