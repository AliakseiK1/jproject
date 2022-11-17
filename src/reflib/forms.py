from dataclasses import field
from django import forms

from . import models

class Author(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = ["auth_name","auth_country","auth_note"]


class Publisher(forms.ModelForm):
    class Meta:
        model = models.Publisher
        fields = ["pub_name","pub_country","pub_note"]
