from dataclasses import field
from django import forms

from . import models

"""
class Author(forms.Form):
    auth_name = forms.CharField(
        max_length=100,
        label="Name of Author",
        help_text="Type the name",
        required=YES)
    auth_country = forms.CharField(
        max_length=100,
        label="Country of Origination",
        help_text="Provide the name",
        required=YES)
    auth_note = forms.CharField(widget=forms.Textarea)
"""
class Author(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = ["auth_name","auth_country","auth_note"]


class Publisher(forms.ModelForm):
    class Meta:
        model = models.Publisher
        fields = ["pub_name","pub_country","pub_note"]
