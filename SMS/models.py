
from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)
    address=models.TextField()
    mobileno=models.CharField(max_length=15)
    dob=models.DateField(null=True,blank=True)
    pic=models.ImageField(null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    last_updated_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class course(models.Model):
    name=models.CharField(max_length=50)
    students=models.ManyToManyField(student,null=True,blank=True)
    def __str__(self):
        return self.name

class paymentDetials(models.Model):
    amount=models.IntegerField()
    payment_mode=models.CharField(max_length=100,choices=[('Cash','Cash'),('Debit Card','Debit Card'),('Credit Card','Credit Card'),('Paytm','Paytm')])
    payment_date=models.DateField(auto_now=True)
    student=models.ForeignKey(student,null=False,blank=False,on_delete=models.CASCADE)

    
