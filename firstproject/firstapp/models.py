from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    company = models.CharField(max_length=100)