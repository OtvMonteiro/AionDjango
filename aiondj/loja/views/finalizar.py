from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from django.views import View

from loja.templatetags.custom_filter import multiply

from loja.models.produto import Produtos
from loja.models.venda import Vendas


class Finalizar(View):
    def post(self, request):
        quantidade = request.POST.get('quantidade')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        
        checkout = request.session.get('checkout')
        produtos = Produtos.get_produtos_by_id(list(checkout.keys()))
        
        
        print(email, cpf, nome, endereco, produtos)

        for produto in produtos:
            print(checkout.get(str(produto.id)))
            venda = Vendas(email = email,
                          cpf = cpf,
                          nome = nome, 
                          endereco=endereco,
                          id_produto=produto.id,
                          quantidade=int(quantidade or 0),
                          valor_total = multiply(int(quantidade or 0), produto.preco_unitario))
            venda.save()
        request.session['checkout'] = {}

        return redirect('checkout')
