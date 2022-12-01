from dataclasses import field
from django import forms
from . import models


class Cart(forms.ModelForm):
    class Meta:
        model = models.Cart
        fields = ["user"]

class CartItem(forms.ModelForm):
    class Meta:
        model = models.CartItem
        fields = ["book","quantity","price_ht","cart"]


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ["name_surname","address_line1","address_line2","town_city","country","phone_number","email"]
        
