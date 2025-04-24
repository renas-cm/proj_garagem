from django.db import models

class Cor(models.Model):
    nome = models.CharField(max_length=40, verbose_name='Nome')
    
    def __str__(self):
        return f'{self.nome}'