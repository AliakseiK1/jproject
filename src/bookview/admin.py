from django.contrib import admin
from reflib import models
from bookview import models
# Register your models here.

#Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('pk', 'book_image', 'book_name', 'book_aut', 'publisher', 'book_annotation','book_cover','category','price_ht','created_at','created_by')
admin.site.register(models.Book, BookAdmin)