from collections.abc import Iterable
from django.db import models
from users.models import Contact
from django.contrib.auth.models import User

# Create your models here.

## The important Models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    quantity = models.IntegerField()
    buyingPrice = models.IntegerField()
    sellingPrice = models.IntegerField()
    discountPrice = models.IntegerField(default=0)

    location = models.CharField(blank=True, null=True, max_length=1000)

    def __str__(self):
        return self.name
    

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    priceSold = models.IntegerField()
    dateTime = models.DateTimeField(auto_now_add=True)
    paymentMethod = models.CharField(max_length=10)
    buyer = models.ForeignKey(Contact, blank=True, null=True, on_delete=models.SET_NULL)
    seller = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.product.name
































class ProtectorType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class CaseType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Phone(models.Model):
    company = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=100)
    
    cameras = models.CharField(max_length=300, blank=True, null=True)
    memory = models.CharField(max_length=300, blank=True, null=True)
    screen = models.CharField(max_length=300, blank=True, null=True)
    battery = models.IntegerField(blank=True, null=True)
    

    quantity = models.IntegerField(default=0)
    buyingPrice = models.IntegerField()
    sellingPrice = models.IntegerField()
    discountPrice = models.IntegerField(blank=True, null=True)

    other = models.TextField(blank=True, null=True)

    location = models.CharField(blank=True, null=True, max_length=1000)

    def __str__(self):
        return self.name
    


class Protector(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    buyingPrice = models.IntegerField(blank=True, null=True)
    sellingPrice = models.IntegerField(blank=True, null=True)
    type = models.ForeignKey(ProtectorType, on_delete=models.CASCADE)
    location = models.CharField(blank=True, null=True, max_length=1000)

    def __str__(self):
        return f"{self.phone.name} | {self.type}"



class Case(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    buyingPrice = models.IntegerField(blank=True, null=True)
    sellingPrice = models.IntegerField(blank=True, null=True)
    type = models.ForeignKey(CaseType, on_delete=models.CASCADE)
    location = models.CharField(blank=True, null=True, max_length=1000)

    def __str__(self):
        return self.phone.name
    


