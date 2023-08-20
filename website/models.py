from django.db import models

# Create your models here.

class ProtectorType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class CaseType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Phone(models.Model):
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    buyingPrice = models.IntegerField()
    sellingPrice = models.IntegerField()
    discountPrice = models.IntegerField(blank=True, null=True)
    ram = models.IntegerField(blank=True, null=True)
    rom = models.IntegerField(blank=True, null=True)
    battery = models.IntegerField(blank=True, null=True)
    screenSize = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    


class Protector(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    buyingPrice = models.IntegerField(blank=True, null=True)
    sellingPrice = models.IntegerField(blank=True, null=True)
    type = models.ForeignKey(ProtectorType, on_delete=models.CASCADE)

    def __str__(self):
        return self.phone.name



class Case(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    buyingPrice = models.IntegerField(blank=True, null=True)
    sellingPrice = models.IntegerField(blank=True, null=True)
    type = models.ForeignKey(CaseType, on_delete=models.CASCADE)

    def __str__(self):
        return self.phone.name


