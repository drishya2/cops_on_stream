from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class My_User(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()
    password=models.CharField(max_length=50)
    type=models.IntegerField()

    def __str__(self):
        return self.username

class Police(models. Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    no_cases=models.IntegerField()
    def __str__(self):
        return self.username

class Case(models.Model):
    case=models.CharField(max_length=50)
    date=models.DateField()
    user=models.ForeignKey(My_User,on_delete=models.CASCADE)
    police=models.ForeignKey(Police,on_delete=models.CASCADE)
    is_completed=models.BooleanField(default=False)





