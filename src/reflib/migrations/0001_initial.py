# Generated by Django 4.1.2 on 2022-11-24 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_name', models.CharField(max_length=100, unique=True, verbose_name='Author Name')),
                ('auth_country', models.CharField(max_length=100, verbose_name='Author Origin')),
                ('auth_note', models.TextField(blank=True, max_length=100, null=True, verbose_name='Note')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types_of_categories', models.CharField(choices=[('SL', 'Sale'), ('NA', 'New Arrival'), ('NC', 'No Category')], default='NC', max_length=2, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types_of_cover', models.CharField(choices=[('HC', 'Hard Cover'), ('SC', 'Softcover'), ('DJ', 'Dust Jacket')], default='HC', max_length=2, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_name', models.CharField(max_length=100, unique=True, verbose_name='Publisher Name')),
                ('pub_country', models.CharField(max_length=100, verbose_name='Publisher Origin')),
                ('pub_note', models.TextField(blank=True, max_length=100, null=True, verbose_name='Note')),
            ],
        ),
    ]
