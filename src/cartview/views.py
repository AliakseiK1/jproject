from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from . import models, forms
from . forms import OrderForm
from . models import Cart, CartItem
from bookview import models as bw_models
from random import randint
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
            books_in_cart, created = models.CartItem.objects.get_or_create(
                book=book,
                cart=cart,
                total=obj_price*int(quantity),
                defaults={
                    "quantity":quantity,
                    "price_ht":obj_price,
                    }
            )
            if not created: ##bug - sometimes on attempt to add the same item - duplicaiton of recorsds, selection of 3 records instead of 1
                books_in_cart.quantity = books_in_cart.quantity + int(quantity)
                books_in_cart.total = obj_price * int(books_in_cart.quantity)
                books_in_cart.save()
    else:
        cart_id = request.session.get('cart_id')
        if cart_id:
            cart = models.Cart.objects.get(pk=cart_id)
            context['cart'] = cart
    context['form'] = forms.OrderForm
    return render(
        request,
        template_name='cartview/cart.html',
        context = context
        )
##-------------- CartItem Views --------------------------------------

class Order(CreateView):
    template_name = "cartview/submit_order.html"
    models = models.Order
    form_class = forms.OrderForm
    success_url = reverse_lazy("cartview:submit_success")
    def form_valid(self, form):
        cart = models.Cart.objects.get(pk=self.request.session.get('cart_id'))
        form.instance.cart = cart
        obj = models.OrderStatus.objects.get(types_of_statuses__contains='new')
        form.instance.status = obj
        return super().form_valid(form)
         
    def get_success_url(self) -> str:
        del self.request.session["cart_id"]
        return super().get_success_url()

class OrderSuccess(TemplateView):
    model = models.Order
    template_name = "cartview/submit_success.html"
    
class MyOrders(ListView):
    template_name = "cartview/my_orders.html"
    model = models.Order
    form_class = forms.MyOrders
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

class UpdOrder(generic.UpdateView):
    model = models.Order
    form_class = forms.EditOrders
    template_name = 'cartview/order_add.upd.html'
    success_url = reverse_lazy("cartview:my_orders")
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Update'
        return context