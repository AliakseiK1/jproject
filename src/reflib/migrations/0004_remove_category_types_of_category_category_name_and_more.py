# Generated by Django 4.1.2 on 2022-11-14 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reflib', '0003_alter_book_category_alter_book_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='types_of_category',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='types_of_categories',
            field=models.CharField(choices=[('SL', 'Sale'), ('NA', 'New Arrival'), ('NC', 'No Category')], default='NA', max_length=2),
        ),
    ]