from django.db import models
from django.contrib.auth import get_user_model
from bookview.models import Book


User = get_user_model()
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="carts", verbose_name="User Cart", null=True,blank=True)
    created_at = models.DateTimeField('Created At',auto_now=False, auto_now_add=True
    )
    
   
    def total_price(self):
        all_items_in_cart = self.bookview.all()
        total_price = 0
        for item_in_cart in all_items_in_cart:
            total_price += item_in_cart.price_per_item
        return total_price

class CartItem(models.Model):
    book = models.ForeignKey("bookview.Book", on_delete=models.PROTECT, verbose_name='book_in_cart')
    quantity = models.IntegerField(default=1, verbose_name='Quantity')
    price_ht = models.DecimalField('Price', blank=True, max_digits=5, decimal_places=2)
    cart = models.ForeignKey("cartview.Cart", on_delete=models.CASCADE, verbose_name='Cart', related_name='bookview')
    total = models.DecimalField(verbose_name='Total', max_digits=5, decimal_places=2)
    created_at = models.DateTimeField('Created At',auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True, auto_now_add=False)

    @property
    def price_per_item(self):
        return self.price_ht * int(self.quantity)

class OrderStatus(models.Model):
    TYPES_OF_STATUSES = [
        ('new', 'New Order'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]
    types_of_statuses = models.CharField(max_length=20, choices=TYPES_OF_STATUSES, default ='new',unique=True)
    def __str__(self):
        return self.types_of_statuses

class Order(models.Model):
    status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Order Status')
    cart = models.OneToOneField("cartview.Cart", on_delete=models.PROTECT, verbose_name='Cart', related_name='order')
    name_surname = models.CharField(verbose_name="First and Last Name", blank=False, max_length=40)
    address_line1 = models.CharField(verbose_name="Address Line 1", blank=False, max_length=60)
    address_line2 = models.CharField(verbose_name="Address Line 2", blank=True, max_length=60)
    town_city = models.CharField(verbose_name="Town/City", blank=False, max_length=60)
    country = models.CharField(verbose_name="Country", blank=False, max_length=60)
    phone_number = models.CharField(verbose_name="Phone Number",blank=True, max_length=60)
    email = models.EmailField(verbose_name="Email", blank=False, max_length=100)
    created_at = models.DateTimeField('Created At',auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True, auto_now_add=False)
    order_comment = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Comment for Order')
