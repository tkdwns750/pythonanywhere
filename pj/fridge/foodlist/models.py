from django.db import models

# Create your models here.

class List(models.Model):
    num = models.PositiveIntegerField
    bar_no = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    life = models.CharField(max_length=50)
