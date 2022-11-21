from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from . import models
from . models import Cart, CartItem
from reflib import models as bw_models

##-------------- Cart Views --------------------------------------
def cart(request):
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
                defaults={'user': user}
            )
            if created:
                request.session['cart_id'] = cart.pk
            cart_item = bw_models.Book.objects.get(pk=int(book_pk))
    return render(
        request=request,
        template_name="cartview/cart.thml", context=context
    )

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