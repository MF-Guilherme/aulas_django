from django.db import models

class Cargo(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    senha = models.CharField(max_length=100)
    cargo = models.ManyToManyField(Cargo)

    def __str__(self):
        return self.nome