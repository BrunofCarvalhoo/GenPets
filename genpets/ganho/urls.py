from django.urls import path
from . import views

urlpatterns = [
    path('', views.ganho, name='ganho'),
    path('cadastrar/', views.cadastrar_animal_view, name='cadastrar_animal'),
    path('salvar/', views.salvar_animal_view, name='salvar_animal'),
]
