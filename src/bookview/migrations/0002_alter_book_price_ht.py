# Generated by Django 4.1.2 on 2022-11-28 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookview', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price_ht',
            field=models.DecimalField(blank=True, decimal_places=2, default='1.00', max_digits=5, verbose_name='Price of the Book'),
        ),
    ]
