from django.contrib import admin
from django.urls import path
from .views.home import Index , loja
from .views.checkout import Checkout
from .views.finalizar import Finalizar
from .middlewares.auth import  auth_middleware



urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('loja', loja , name='loja'),

    path('finalizar', Finalizar.as_view() , name='finalizar'),
    path('checkout', Checkout.as_view() , name='checkout'),
    #path('checkout', auth_middleware(Checkout.as_view()) , name='checkout'),
] 
