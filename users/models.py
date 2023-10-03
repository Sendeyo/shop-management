from django.db import models

class ContactCategory(models.Model):
    name = models.CharField(max_length=100)


class Contact(models.Model):
    name = models.CharField(max_length=300)
    category = models.ForeignKey(ContactCategory, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13)
    description = models.TextField(null=True, blank=True)
