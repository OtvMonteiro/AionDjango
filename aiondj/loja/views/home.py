from django.shortcuts import render , redirect , HttpResponseRedirect
from loja.models.produto import Produtos
from django.views import View


class Index(View):

    def post(self , request):
        produto = request.POST.get('produto')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        cart = {}
        cart[produto] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('checkout')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/loja{request.get_full_path()[1:]}')

def loja(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    produtos = None
    produtos = Produtos.get_all_produtos();  

    data = {}
    data['produtos'] = produtos

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)


