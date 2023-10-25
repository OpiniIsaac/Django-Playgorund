from django.db import models

# Create your models here.
class Product(models.Model):
     title = models.CharField(max_length=255)
     description = models.TextField()
     price = models.DecimalField(max_digits=6, decimal_places=2)
     inventory = models.IntegerField()
     last_placed = models.DateField(auto_now=True)

class Customer(models.Model):
     first_name = models.CharField(max_length=255)
     last_name = models.CharField(max_length=255)
     email = models.EmailField(unique=True)
     phone_number = models.CharField( max_length=50)
     date_of_birth = models.DateField(null=True)

