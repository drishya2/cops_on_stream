from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class My_User(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    type=models.IntegerField()
    pic=models.FileField()

    def __str__(self):
        return self.username

class Police(models. Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    rank=models.CharField(max_length=50)
    pic=models.FileField()
    badge_number=models.IntegerField()
    age=models.IntegerField()
    service_years=models.IntegerField()

    def __str__(self):
        return self.username

class Case(models.Model):
    type_choices=(
        ('m','murder'),
        ('k','kidnapping'),
        ('d','damaging property'),
        ('r','rape'),
        ('p','physical or mental abuse'),
        ('t','theft'),
        ('o','others')

    )
    type=models.CharField(choices=type_choices,max_length=50)
    # case=models.CharField(max_length=50)
    date=models.DateField()
    # completed_date=models.DateField()
    # user=models.ForeignKey(My_User,on_delete=models.CASCADE)
    # police=models.ForeignKey(Police,on_delete=models.CASCADE)
    # is_completed=models.BooleanField(default=False)
    place=models.CharField(max_length=50)
    culprit=models.CharField(max_length=50)
    describe=models.CharField(max_length=50)
    user=models.ForeignKey(My_User,on_delete=models.CASCADE)






