from django.db import models


# Create your models here.

class Price(models.Model):
    marketname = models.CharField(max_length=30)
    dates = models.CharField(max_length=30)
    mclassname = models.CharField(max_length=30)
    avgprice = models.DecimalField(max_digits=10, decimal_places=2)
    minprice = models.DecimalField(max_digits=10, decimal_places=2)
    maxprice = models.DecimalField(max_digits=10, decimal_places=2)
    predict_price = models.DecimalField(max_digits=10, decimal_places=2)
