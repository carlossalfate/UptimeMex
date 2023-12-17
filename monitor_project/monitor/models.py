from django.db import models

class Sucursal(models.Model):
    sucursal = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    active = models.BooleanField()
    region = models.CharField(max_length=100)