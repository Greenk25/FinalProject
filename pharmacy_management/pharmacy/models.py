from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class medicine(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_date = models.DateField()
    category = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Customer(models.Model):

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    contact = models.CharField(max_length=15)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

