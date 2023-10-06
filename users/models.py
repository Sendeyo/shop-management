from django.db import models

class Contact(models.Model):
    CATEGORY_CHOICES = [
        ("customer", "Customer"),
        ("supplier", "Supplier")
    ]

    name = models.CharField(max_length=300)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    phone = models.CharField(max_length=13, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.category})"



class Debt(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("paid", "Paid")
    ]
    THE_CATEGORY_CHOICES = [
        ("owed", "Owed"),
        ("owing", "Owing")
    ]
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    amount = models.IntegerField()
    category = models.CharField(max_length=20, choices=THE_CATEGORY_CHOICES, null=True)
    due_date = models.DateField(null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.contact.name