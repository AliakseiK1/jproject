from django.db import models
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib.auth import settings
from reflib.models import Author, Publisher, Cover, Category

class Book(models.Model):
    book_image = models.ImageField(
        verbose_name="Book Image",
        upload_to="uploads/%Y/%m/%d/"    
    )
    book_name = models.CharField(
        max_length=100,
        verbose_name='Book Name')
    book_aut = models.ForeignKey(Author, on_delete=models.PROTECT, blank=True, verbose_name='Book Author')
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, blank=True, verbose_name='Publisher', default=1)
    book_annotation = models.TextField(
        max_length=500,
        blank=False,
        null=False,
        verbose_name='Annotation')
    book_cover = models.ForeignKey(Cover, on_delete=models.CASCADE, blank=True, verbose_name='Book Cover')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, verbose_name='Category')
    price_ht = models.FloatField(verbose_name='Price of the Book', default='1.00')
    created_at = models.DateTimeField(default=datetime.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, on_delete=models.PROTECT) 
    def __str__(self):
        return self.book_name
    

    def get_absolute_url(self):
        #return f'/details_author/{self.pk}'
        return reverse_lazy('bookview:details_book', kwargs=({'pk': self.pk}))
    
    TVA_AMOUNT = 19.25

    def price_ttc(self):
        return self.price_ht + self.TVA_AMOUNT