# Generated by Django 4.1.2 on 2022-10-09 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reflib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_name', models.CharField(max_length=100, verbose_name='Author Name')),
                ('auth_country', models.CharField(max_length=100, verbose_name='Author Origin')),
                ('auth_note', models.TextField(blank=True, max_length=100, null=True, verbose_name='Note')),
            ],
        ),
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types_of_cover', models.CharField(choices=[('HC', 'Hard Cover'), ('SC', 'Sophomore'), ('DJ', 'Dust Jacket')], default='HC', max_length=2)),
            ],
        ),
    ]