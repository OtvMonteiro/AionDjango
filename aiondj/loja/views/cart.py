from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from django.views import  View
from loja.models.produto import Produtos

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        produtos = Produtos.get_produtos_by_id(ids)
        print(produtos)
        #return render(request , 'cart.html' , {'produtos' : produtos} )
 
