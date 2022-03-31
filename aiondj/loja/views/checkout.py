from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from django.views import View

from loja.templatetags.custom_filter import multiply

from loja.models.produto import Produtos
from loja.models.venda import Vendas


class CheckOut(View):
    def post(self, request):
        quantidade = request.POST.get('quantidade')
       
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        
        cart = request.session.get('cart')
        produtos = Produtos.get_produtos_by_id(list(cart.keys()))
        
        
        print(email, cpf, nome, endereco, produtos)

        for produto in produtos:
            print(cart.get(str(produto.id)))
            venda = Vendas(email = email,
                          cpf = cpf,
                          nome = nome, 
                          endereco=endereco,
                          id_produto=produto,
                          quantidade=int(quantidade or 0),
                          valor_total = multiply(int(quantidade or 0), produto.preco_unitario))
            venda.save()
        request.session['cart'] = {}

        return redirect('homepage')
