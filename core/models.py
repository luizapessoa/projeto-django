from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.nome
