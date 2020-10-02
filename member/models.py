from django.db import models
import uuid

# Create your models here.
class Member(models.Model):
    id_member   = models.AutoField(primary_key=True)
    email       = models.EmailField(max_length=128, unique=True)
    name        = models.CharField(max_length=40)
    sex         = models.CharField(max_length=1)
    birth_date      = models.DateField()
    register_date   = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'bajigur_member'


class Transaction(models.Model):
    id_trx = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    id_member   = models.IntegerField()
    id_item     = models.IntegerField()
    qty         = models.IntegerField(default=1)
    total       = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    trx_date    = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'bajigur_transaction'
        ordering = ['-trx_date']


class WishList(models.Model):
    id_wishlist = models.AutoField(primary_key=True)
    id_member = models.IntegerField()
    id_item = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'bajigur_wishlist'
