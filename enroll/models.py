from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField()
    password=models.CharField(max_length=70)