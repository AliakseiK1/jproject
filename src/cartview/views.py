from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models
from . models import Cart, CartItem
from bookview import models as bw_models
from random import randint


def cart(request, *args, **kwargs):
    context = {}
    if request.method == "POST":
        book_pk = request.POST.get('book_pk')
        quantity = request.POST.get('quantity')
        if book_pk and quantity:
            cart_id = int(request.session.get('cart_id',0))
            if request.user.is_authenticated:
                user = request.user
            else:
                user = None
            if cart_id == 0:
                cart_id = None
            cart, created = models.Cart.objects.get_or_create(
                pk=cart_id,
                defaults={"user": user}
            )
            if created:
                request.session['cart_id'] = cart.pk
            book = bw_models.Book.objects.get(pk=int(book_pk))
            obj = bw_models.Book.objects.get(pk=int(book_pk))
            obj_price = int(obj.price_ht)
            books_in_cart = models.CartItem.objects.create(
                book=book,
                cart=cart,
                quantity=quantity,
                price_ht=obj_price,
                total = round(float(obj_price*quantity),2)
                )
        
        return render(request=request,
    template_name="cartview/cart.html",
    context=context)


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

"""
class ViewCartItem(generic.TemplateView):
    model = CartItem
    template_name='cartview/cartitem_view.html'

"""

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