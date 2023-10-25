from django.db import models

# Create your models here.
class Product(models.Model):
     title = models.CharField(max_length=255)
     description = models.TextField()
     price = models.DecimalField(max_digits=6, decimal_places=2)
     inventory = models.IntegerField()
     last_placed = models.DateField(auto_now=True)

class Customer(models.Model):
     MEMBERSHIP_BRONZE = 'B'
     MEMBERSHIP_SILVER = 'S'
     MEMBERSHIP_GOLD = 'G'
     MEMBERSHIP_CHOICES = [
          (MEMBERSHIP_BRONZE,'Bronze'),
          (MEMBERSHIP_SILVER, 'Silver'),
          (MEMBERSHIP_GOLD,'Gold')
     ]
     first_name = models.CharField(max_length=255)
     last_name = models.CharField(max_length=255)
     email = models.EmailField(unique=True)
     phone_number = models.CharField( max_length=50)
     date_of_birth = models.DateField(null=True)
     membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONZE)
class Address (models.Model):
     street = models.CharField(max_length=255)
     city = models.CharField(max_length=255)
     customer = models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)     
class Order(models.Model):
     PENDING = 'P'
     COMPLETE = 'C'
     FAILED = 'F'
     PAYMENT_STATUS = [
          (PENDING,'Pending'),
          (COMPLETE,'Complete'),

          (FAILED,'Failed')
     ]
     played_at = models.DateField(auto_now_add=True)
     payment_status = models.CharField(max_length=1,choices=PAYMENT_STATUS,default=PENDING)