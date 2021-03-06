# Generated by Django 3.1.1 on 2020-10-01 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Featured',
            fields=[
                ('id_feature', models.AutoField(primary_key=True, serialize=False)),
                ('id_item', models.IntegerField()),
                ('feature_expiry', models.DateTimeField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id_item', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('size', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(max_length=1024)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OnSale',
            fields=[
                ('id_sale', models.AutoField(primary_key=True, serialize=False)),
                ('id_item', models.IntegerField()),
                ('sale_expiry', models.DateTimeField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
