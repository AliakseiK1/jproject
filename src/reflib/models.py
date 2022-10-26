from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class Publisher(models.Model):
    pub_name = models.CharField(
        max_length=100,
        #blank=True,
        #null=True
        verbose_name='Publisher Name')
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

class Author(models.Model):
    auth_name = models.CharField(
        max_length=100,
        verbose_name='Author Name')
    auth_country = models.CharField(
        max_length=100,
        verbose_name='Author Origin')
    auth_note = models.TextField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Note')
    def get_absolute_url(self):
        #return f'/details_author/{self.pk}'
        return reverse_lazy('reflib:details_author', kwargs={'pk': self.pk})

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
    )
    def is_upperclass(self):
        return self.types_of_cover in {self.HARDCOVER, self.DUSTCOVER}


def __str__(self):
    return self.name

def __repr__(self):
    return self.name
