from django.db import models


# Create your models here.

class Price(models.Model):
    DELNG_DE = models.CharField(max_length=30)
    MRKT_NM = models.CharField(max_length=30)
    CPR_NM = models.CharField(max_length=30)
    PRDLST_NM = models.CharField(max_length=30)
    SPCIES_NM = models.CharField(max_length=30)
    GRAD = models.CharField(max_length=30)
    weight = models.CharField(max_length=30)
    PRI_MAX = models.DecimalField(max_digits=10, decimal_places=2)
    PRI_MIN = models.DecimalField(max_digits=10, decimal_places=2)
    PRI_AVE = models.DecimalField(max_digits=10, decimal_places=2)
    PRI_PRED = models.DecimalField(max_digits=10, decimal_places=2)
