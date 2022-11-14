from dataclasses import field
from django import forms

from . import models


class Cart(forms.ModelForm):
    class Meta:
        model = models.Cart
        fields = ["user","created_at"]

class CartItem(forms.ModelForm):
    class Meta:
        model = models.CartItem
        fields = ["book","quantity","price_ht","cart"]