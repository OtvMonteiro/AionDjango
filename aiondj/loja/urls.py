from django.contrib import admin
from django.urls import path
from .views.home import Index , loja
from .views.cart import Cart
from .views.checkout import CheckOut
from .middlewares.auth import  auth_middleware



urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('loja', loja , name='loja'),

    path('checkout', CheckOut.as_view() , name='checkout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
] 
