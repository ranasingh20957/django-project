from django.db import models

# Create your models here.
class Employes(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    salary=models.IntegerField()
    post=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    def _str_(self):
        return self.name
