# Generated by Django 4.1.2 on 2022-11-28 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartview', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Total'),
        ),
    ]
