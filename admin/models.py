from django.db import models

# Create your models here.
class Item(models.Model):
    id_item = models.AutoField(primary_key=True)
    name    = models.CharField(max_length=40)
    size    = models.IntegerField()
    price   = models.DecimalField(decimal_places=2, max_digits=10)
    category    = models.CharField(max_length=1024)
    date_added  = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'bajigur_items'


class OnSale(models.Model):
    id_sale     = models.AutoField(primary_key=True)
    id_item     = models.IntegerField()
    discount    = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    sale_start  = models.DateTimeField(default=None)
    sale_expiry = models.DateTimeField(default=None)
    date_added  = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'bajigur_onsale'


class Featured(models.Model):
    id_feature  = models.AutoField(primary_key=True)
    id_item     = models.IntegerField()
    feature_start   = models.DateTimeField(default=None)
    feature_expiry  = models.DateTimeField(default=None)
    date_added      = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'bajigur_featured'
