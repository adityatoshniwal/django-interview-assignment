from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=10)