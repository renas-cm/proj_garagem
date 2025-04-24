from django.db import models

class Modelo(models.Model):
    nome = models.CharField(max_length=80, verbose_name='Nome', blank=True)
    marca = models.CharField(max_length=80, verbose_name='Marca', blank=True)
    categoria = models.CharField(max_length=80, verbose_name='Categoria', blank=True)
    
    def __str__(self):
        return f'{self.nome.upper()}, {self.marca.upper()}'