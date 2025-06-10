from django.db import models

class Veiculo(models.Model):
    ano = models.IntegerField(verbose_name='Ano', null=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço', null=True, default=0)
    modelo = models.ForeignKey('Modelo', on_delete=models.CASCADE, verbose_name='Modelo')
    cor = models.ForeignKey('Cor', on_delete=models.CASCADE, verbose_name='Cor')
    acessorios = models.ManyToManyField('Acessorio', blank=True, verbose_name='Acessórios')
    
    def __str__(self):
        return f'{self.modelo}, {self.cor}, {self.ano}'
    