from django.db import models

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=50)
    barcode=models.CharField(max_length=50)
    model=models.CharField(max_length=50)
    price=models.FloatField()
    qty=models.IntegerField()
    active=models.BooleanField()
    class Meta:
        db_table="product_info"

class Vendor(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    product=models.ManyToManyField(product)
    class Meta:
        db_table="vendor_info"