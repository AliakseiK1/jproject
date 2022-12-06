from django.contrib import admin
from reflib import models

# Register your models here.

admin.site.register(models.Cover)
admin.site.register(models.Category)

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('pk', 'pub_name', 'pub_country', 'pub_note')
admin.site.register(models.Publisher, PublisherAdmin)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'auth_name', 'auth_country', 'auth_note')
admin.site.register(models.Author, AuthorAdmin)