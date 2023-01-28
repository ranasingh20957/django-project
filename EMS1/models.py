from django.db import models

# Create your models here.
class Employes(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    mobileno=models.CharField(max_length=10)
    city=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    img=models.ImageField()
    def _str_(self):
     return self.name
        