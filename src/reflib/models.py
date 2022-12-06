from typing import Generic
from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class Publisher(models.Model):
    pub_name = models.CharField(
        max_length=100,
        verbose_name='Publisher Name',
        unique=True)
    pub_country = models.CharField(
        max_length=100,
        verbose_name='Publisher Origin')
    pub_note = models.TextField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Note')
    def get_absolute_url(self):
        return reverse_lazy('reflib:details_publisher', kwargs={'pk': self.pk})
    class Meta:
        ordering = ['pk']
    def __str__(self):
        return self.pub_name
    

class Author(models.Model):
    auth_name = models.CharField(
        max_length=100,
        verbose_name='Author Name',
        unique=True)
    auth_country = models.CharField(
        max_length=100,
        verbose_name='Author Origin')
    auth_note = models.TextField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Note')
    def get_absolute_url(self):
        return reverse_lazy('reflib:details_author', kwargs={'pk': self.pk})
    class Meta:
        ordering = ['pk']
    def __str__(self):
        return self.auth_name

class Cover(models.Model):
    HADRCOVER = 'HC'
    SOFTCOVER = 'SC'
    DUSTJACKET = 'DJ'
    TYPES_OF_COVER_CHOICES = [
        (HADRCOVER, 'Hard Cover'),
        (SOFTCOVER, 'Softcover'),
        (DUSTJACKET, 'Dust Jacket'),
    ]
    types_of_cover = models.CharField(
        max_length=2,
        choices=TYPES_OF_COVER_CHOICES,
        default=HADRCOVER,
        unique=True,
    )
    def __str__(self):
        return self.types_of_cover
    

class Category(models.Model):
    TYPES_OF_CATEGORIES = [
        ('SL', 'Sale'),
        ('NA', 'New Arrival'),
        ('NC', 'No Category'),
    ]
    types_of_categories = models.CharField(max_length=2, choices=TYPES_OF_CATEGORIES, default = 'NC',unique=True)
    def __str__(self):
        return self.types_of_categories