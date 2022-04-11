
from django.db import models

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=15)
    roll_no = models.IntegerField()
    Class=models.CharField(max_length=10)
    #mobile=models.IntegerField()