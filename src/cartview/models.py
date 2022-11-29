from django.db import models
from django.contrib.auth import get_user_model
from bookview.models import Book

User = get_user_model()
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="carts", verbose_name="User Cart", null=True,blank=True)
    created_at = models.DateTimeField('Created At',auto_now=False, auto_now_add=True)

class CartItem(models.Model):
    book = models.ForeignKey("bookview.Book", on_delete=models.PROTECT, verbose_name='book_in_cart')
    quantity = models.IntegerField(default=1, verbose_name='Quantity')
    price_ht = models.DecimalField('Price', blank=True, max_digits=5, decimal_places=2)
    cart = models.ForeignKey("cartview.Cart", on_delete=models.CASCADE, verbose_name='Cart', related_name='bookview')
    total = models.DecimalField(verbose_name='Total', max_digits=5, decimal_places=2)
    created_at = models.DateTimeField('Created At',auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True, auto_now_add=False)