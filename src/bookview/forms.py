from dataclasses import field
from django import forms

from reflib import models


class Book(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ["book_image","book_name","book_aut","book_annotation", "book_cover"]