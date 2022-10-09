from django.db import models

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

from django.db import models

class Cover(models.Model):
    HADRCOVER = 'HC'
    SOFTCOVER = 'SC'
    DUSTJACKET = 'DJ'
    TYPES_OF_COVER_CHOICES = [
        (HADRCOVER, 'Hard Cover'),
        (SOFTCOVER, 'Sophomore'),
        (DUSTJACKET, 'Dust Jacket'),
    ]
    types_of_cover = models.CharField(
        max_length=2,
        choices=TYPES_OF_COVER_CHOICES,
        default=HADRCOVER,
    )

def is_upperclass(self):
        return self.types_of_cover in {self.HARDCOVER, self.DUSTCOVER}