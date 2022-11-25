from django.contrib import admin
from reflib import models

# Register your models here.

admin.site.register(models.Publisher)
admin.site.register(models.Author)
admin.site.register(models.Cover)
admin.site.register(models.Category)

from bookview import models

#Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('pk', 'book_image', 'book_name', 'book_aut', 'publisher', 'book_annotation','book_cover','category','price_ht','created_at','created_by')
admin.site.register(models.Book, BookAdmin)

#cartview
from cartview import models

class CartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user')
admin.site.register(models.Cart, CartAdmin)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("pk", "book", "quantity", "price_ht", "cart","total","created_at","updated_at")
admin.site.register(models.CartItem, CartItemAdmin)