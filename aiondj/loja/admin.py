from django.contrib import admin
from .models.produto import Produtos
from .models.venda import Vendas

# Register your models here.
admin.site.register(Produtos)
admin.site.register(Vendas)