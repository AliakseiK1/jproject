# Generated by Django 4.1.2 on 2022-12-06 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartview', '0014_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_comment',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Comment for Order'),
        ),
    ]