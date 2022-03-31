from django.shortcuts import render , redirect , HttpResponseRedirect
from loja.models.produto import Produtos
from django.views import View


class Index(View):

    def post(self , request):
        produto = request.POST.get('produto')
        remove = request.POST.get('remove')
        checkout = request.session.get('checkout')
        checkout = {}
        checkout[produto] = 1

        request.session['checkout'] = checkout
        print('checkout' , request.session['checkout'])
        return redirect('checkout')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/loja{request.get_full_path()[1:]}')

def loja(request):
    checkout = request.session.get('checkout')
    if not checkout:
        request.session['checkout'] = {}
    produtos = None
    produtos = Produtos.get_all_produtos();  

    data = {}
    data['produtos'] = produtos

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)


