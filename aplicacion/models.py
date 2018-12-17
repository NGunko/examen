from __future__ import unicode_literals
from django.db import models
import datetime

class vendedor(models.Model):
    nombreV = models.CharField(max_length=128, unique=True, null=True, blank=True)


class prenda(models.Model):
    nombreP = models.CharField(max_length=128)


class venta(models.Model):
    vendedor = models.ManyToManyField(vendedor)
    prenda = models.ManyToManyField(prenda)
    fechaDeVenta = models.DateField(default=datetime.date.today)
