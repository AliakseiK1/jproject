# Generated by Django 4.1.2 on 2022-11-28 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartview', '0004_alter_cartitem_price_ht_alter_cartitem_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='total',
            field=models.FloatField(verbose_name='Total'),
        ),
    ]
