import datetime
from django.db import models

# Create your models here.


class University(models.Model):
    universityName = models.CharField(max_length=100)

    def __str__(self):
        return self.universityName


class Student(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    age = models.IntegerField()
    qualification = models.CharField(max_length=10)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    reg_date = models.DateField(auto_now_add=True)
    email = models.EmailField()
    password = models.CharField(max_length=20)
