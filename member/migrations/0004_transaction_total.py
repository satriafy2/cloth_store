# Generated by Django 3.1.1 on 2020-10-02 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_transaction_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
