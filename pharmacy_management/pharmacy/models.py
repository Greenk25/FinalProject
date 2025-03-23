from django.db import models

# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    expiry_date = models.DateField()
    supplier = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    contact = models.CharField(max_length=15)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

