from django.contrib import admin
from reflib import models

# Register your models here.

admin.site.register(models.Publisher)
admin.site.register(models.Author)
admin.site.register(models.Cover)
admin.site.register(models.Category)