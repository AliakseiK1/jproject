# Generated by Django 4.1.2 on 2022-11-28 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartview', '0003_alter_cartitem_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='price_ht',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=7, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='total',
            field=models.DecimalField(decimal_places=3, max_digits=7, verbose_name='Total'),
        ),
    ]
