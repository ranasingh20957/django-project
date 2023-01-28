from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    mobileno=models.CharField(max_length=15)
    def __str__(self):
        return self.name

class PresonalDetial(models.Model):
    pic=models.ImageField()
    address=models.CharField(max_length=200)
    student=models.OneToOneField(student,on_delete=models.CASCADE,null=True,blank=True)

@receiver(signal=post_save,sender=student)
def after_save_student(sender,instance,created,**kwargs):
    if created:
        pd=PresonalDetial()
        pd.student=instance
        pd.save()
        
    #print('Post Save Signal Received')
    #print('Sender=',sender)
    #print('Instance=',instance)
    #print('Created=',created)
    

