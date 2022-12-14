# Generated by Django 4.1.2 on 2022-11-30 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cartview', '0011_alter_orderstatus_types_of_statuses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='cartview.orderstatus', verbose_name='Order Status'),
        ),
        migrations.AlterField(
            model_name='orderstatus',
            name='types_of_statuses',
            field=models.CharField(choices=[('new', 'New Order'), ('in_progress', 'In Progress'), ('done', 'Done')], default='new', max_length=20, unique=True),
        ),
    ]
