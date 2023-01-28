from email.headerregistry import Address
from operator import mod
from django.db import models

# Create your models here.
class Customer(models.Model):
    #id=models.IntegerField() #id generate automatically by django
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    mobileno=models.CharField(max_length=15)
    def _str_(self):
       return self.name

class Employee(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    mobileno=models.CharField(max_length=15)
    post=models.CharField(max_length=20)
    salary=models.IntegerField()
    def __str__(self):
        return self.name
