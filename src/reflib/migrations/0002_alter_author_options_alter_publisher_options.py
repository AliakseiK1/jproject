# Generated by Django 4.1.2 on 2022-12-06 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reflib', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['pk']},
        ),
    ]
