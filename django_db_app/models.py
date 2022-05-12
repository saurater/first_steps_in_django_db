from django.db import models

# Create your models here.

class Customers(models.Model):
    first_name= models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FilePathField(path="/img")