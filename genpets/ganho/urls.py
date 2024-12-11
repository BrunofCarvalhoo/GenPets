from django.urls import path
from . import views

urlpatterns = [
    path('', views.ganho, name='ganho'),
    path('cadastrar/', views.cadastrar_animal_view, name='cadastrar_animal'),
    path('salvar/', views.salvar_animal_view, name='salvar_animal'),
    path('editar/<int:id>/', views.editar_animal, name='editar_animal'),
    path('deletar/<int:id>/', views.deletar_animal, name='deletar_animal'),
]
