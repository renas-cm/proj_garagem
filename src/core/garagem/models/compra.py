from django.db import models

from core.usuario.models import Usuario
from . import Veiculo
from django.utils.timezone import now


class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, 'Carrinho'
        REALIZADO = 2, 'Realizado'
        PAGO = 3, 'Pago',
        ENTREGUE = 4, 'Entregue',
    
    class TipoPagamento(models.IntegerChoices):
        CARTAO_CREDITO = 1, "Cartão de Crédito"
        CARTAO_DEBITO = 2, "Cartão de Débito"
        PIX = 3, "PIX"
        BOLETO = 4, "Boleto"
        TRANSFERENCIA_BANCARIA = 5, "Transferência Bancária"
        DINHEIRO = 6, "Dinheiro"
        OUTRO = 7, "Outro"
        
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='compras')
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)
    data = models.DateTimeField(default=now, editable=False)
    tipo_pagamento = models.IntegerField(choices=TipoPagamento.choices, default=TipoPagamento.CARTAO_CREDITO)
    
    
    @property
    def total(self):
        return sum(item.preco_item * item.quantidade for item in self.itens.all())
    
class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, related_name="itens", on_delete=models.CASCADE)
    livro = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name="+")
    preco_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantidade = models.IntegerField(default=1)
    