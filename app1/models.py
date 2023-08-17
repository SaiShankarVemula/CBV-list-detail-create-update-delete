from django.db import models
from django.urls import reverse
# Create your models here.

class School(models.Model):
    Scname=models.CharField(max_length=50)
    Scprinc=models.CharField(max_length=50)
    Scloc=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Scname

    def get_absolute_url(self):
            return reverse('detail',kwargs={'pk':self.pk})
    
class Student(models.Model):
    Sid=models.IntegerField()
    Sname=models.CharField(max_length=30)
    Sage=models.IntegerField()
    Scname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='panda')
    
