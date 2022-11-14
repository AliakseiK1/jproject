from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import Cart, CartItem

##-------------- Cart Views --------------------------------------
class DetailCart(DetailView):
    model = Cart
    template_name='cartview/cart_detail.html'

class ListCart(ListView):
    model = Cart
    context_object_name = 'carts'
    template_name='cartview/carts_list.html'

class CreateCart(CreateView):
    model = Cart
    template_name = 'cartview/cart_create.html'

class UpdateCart(UpdateView):
    model = Cart
    template_name = 'cartview/cart_update.html'

class DeleteCart(DeleteView):
    model = Cart
    template_name = 'cartview/cart_delete.html'


##-------------- CartItem Views --------------------------------------
class DetailCartItem(DetailView):
    model = CartItem
    template_name='cartview/detail_cartitem.html'

class ListCartItem(ListView):
    model = CartItem
    context_object_name = 'cartitems'
    template_name='cartview/cartitems_list.html'

class CreateCartItem(CreateView):
    model = CartItem
    template_name = 'cartview/cartitem_create.html'

class UpdateCartItem(UpdateView):
    model = CartItem
    template_name = 'cartview/cartitem_update.html'

class DeleteCartItem(DeleteView):
    model = Cart
    template_name = 'cartview/cartitem_delete.html'