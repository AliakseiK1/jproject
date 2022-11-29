from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models
from . models import Cart, CartItem
from bookview import models as bw_models
from random import randint
from . import forms
from django.urls import reverse_lazy

class DeleteCartItem(DeleteView):
    model = models.CartItem
    success_url = reverse_lazy("cartview:cart")
    template_name = 'cartview/cartitem_delete.html'


def cart(request, *args, **kwargs):
    context = {}
    context['cart'] = None
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
            context["cart"] = cart
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
                total = obj_price*int(quantity),
                )
    else:
        print(request.user)
        print(request.session.get('cart_id'))
        cart_id = request.session.get('cart_id')
        if cart_id:
            cart = models.Cart.objects.get(pk=cart_id)
            context['cart'] = cart
    return render(
        request,
        template_name='cartview/cart.html',
        context = context
        )
##-------------- CartItem Views --------------------------------------



class UpdCartItem(generic.UpdateView):
    model = models.CartItem
    form_class = forms.CartItem
    template_name = 'cartview/cartitem_add.upd.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Update'
        return context
    