from django.db import models
from .produto import Produtos

import datetime


class Vendas(models.Model):
    email =    models.CharField (max_length=50, default='', blank=True)
    cpf =      models.CharField (max_length=11, default='', blank=True)
    nome =     models.CharField (max_length=50, default='', blank=True)
    endereco = models.CharField (max_length=50, default='', blank=True)
    data = models.DateField (default=datetime.datetime.today)
    id_produto = models.ForeignKey(Produtos,
                                on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def finalizarCompra(self):
        self.save()
        # considerar aqui caso for invalida a compra (estoque<quantidade)?
