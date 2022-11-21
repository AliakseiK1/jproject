from re import template
from typing import Generic
from django.db import models
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views import generic
from datetime import datetime
from django.contrib.auth import settings


# Create your models here.
class Publisher(models.Model):
    pub_name = models.CharField(
        max_length=100,
        #blank=True,
        #null=True
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
        #return f'/details_publisher/{self.pk}'
        return reverse_lazy('reflib:details_publisher', kwargs={'pk': self.pk})
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
    def __str__(self):
        return self.auth_name
    def get_absolute_url(self):
        #return f'/details_author/{self.pk}'
        return reverse_lazy('reflib:details_author', kwargs={'pk': self.pk})
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
    """
    def is_upperclass(self):
        return self.TYPES_OF_COVER_CHOICES in {self.HADRCOVER, self.SOFTCOVER, self.DUSTJACKET}
    """ 

class Category(models.Model):
    TYPES_OF_CATEGORIES = [
        ('SL', 'Sale'),
        ('NA', 'New Arrival'),
        ('NC', 'No Category'),
    ]
    types_of_categories = models.CharField(max_length=2, choices=TYPES_OF_CATEGORIES, default = 'NC',unique=True)
    def __str__(self):
        return self.types_of_categories
   

class MainPage(generic.TemplateView):
    template_name = 'mainpage/mainpage.html'


class Book(models.Model):
    book_image = models.ImageField(
        verbose_name="Book Image",
        upload_to="uploads/%Y/%m/%d/"    
    )
    book_name = models.CharField(
        max_length=100,
        verbose_name='Book Name')
    book_aut = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, verbose_name='Book Author')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, blank=True, verbose_name='Publisher', default=1)
    book_annotation = models.TextField(
        max_length=500,
        blank=False,
        null=False,
        verbose_name='Annotation')
    book_cover = models.ForeignKey(Cover, on_delete=models.CASCADE, blank=True, verbose_name='Book Cover')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, verbose_name='Category')
    price_ht = models.FloatField(verbose_name='Price of the Book', default='1.00')
    created_at = models.DateTimeField(default=datetime.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, on_delete=models.CASCADE) 
    def __str__(self):
        return self.book_name
    

    def get_absolute_url(self):
        #return f'/details_author/{self.pk}'
        return reverse_lazy('bookview:details_book', kwargs=({'pk': self.pk}))
    

    TVA_AMOUNT = 19.25

    def price_ttc(self):
        return self.price_ht + self.TVA_AMOUNT