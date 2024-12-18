from django.urls import path
from . import views

urlpatterns = [
    path('', views.faturamento, name='faturamento'),
    path('adicionar/', views.adicionar_ganho, name='adicionar_ganho'),
    
]
