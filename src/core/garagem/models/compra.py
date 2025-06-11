from django.db import models

from core.usuario.models import Usuario
from . import Veiculo
    
class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, 'Carrinho'
        REALIZADO = 2, 'Realizado'
        PAGO = 3, 'Pago',
        ENTREGUE = 4, 'Entregue',
    
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='compras')
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)
    
class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, related_name="itens", on_delete=models.CASCADE)
    livro = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name="+")
    quantidade = models.IntegerField(default=1)