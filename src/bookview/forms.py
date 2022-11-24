from dataclasses import field
from django import forms
from . import models


class Book(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ["book_image","book_name","book_aut","publisher","book_annotation", "book_cover", "category", "price_ht", "created_at", "created_by"]