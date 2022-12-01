from django.contrib import admin
from . import models

admin.site.register(models.OrderStatus)
class CartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'created_at')
admin.site.register(models.Cart, CartAdmin)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ("pk", "book", "quantity", "price_ht", "cart","total","created_at","updated_at")
admin.site.register(models.CartItem, CartItemAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ("pk", "status", "cart", "name_surname","address_line1", "address_line2","town_city","country","phone_number","email","created_at","updated_at")
admin.site.register(models.Order, OrderAdmin)