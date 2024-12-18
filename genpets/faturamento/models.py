from django.db import models
from ganho.models import Animal  # Importa o modelo Animal do app ganho
from django.utils import timezone

class Ganho(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    data = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.animal.nome} - R$ {self.valor}"
