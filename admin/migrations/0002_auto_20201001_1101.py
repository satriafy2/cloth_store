# Generated by Django 3.1.1 on 2020-10-01 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='featured',
            table='bajigur_featured',
        ),
        migrations.AlterModelTable(
            name='item',
            table='bajigur_items',
        ),
        migrations.AlterModelTable(
            name='onsale',
            table='bajigur_onsale',
        ),
    ]
