from django.db import models

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.PositiveIntegerField()
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=10, choices=[('Macho', 'Macho'), ('Fêmea', 'Fêmea')])
    vacinas = models.TextField(blank=True)

    def __str__(self):
        return self.nome
