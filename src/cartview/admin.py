from django.contrib import admin
from . import models

class CartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'created_at')
admin.site.register(models.Cart, CartAdmin)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ("pk", "book", "quantity", "price_ht", "cart","total","created_at","updated_at")
admin.site.register(models.CartItem, CartItemAdmin)