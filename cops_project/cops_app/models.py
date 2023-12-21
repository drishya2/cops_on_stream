from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    #common fields for both regular users and police
    phone=models.IntegerField(null=True,blank=True)
    address=models.CharField(max_length=50,null=True,blank=True)
    pic=models.FileField()

    rank=models.CharField(max_length=50,blank=True,null=True)
    badge_number=models.IntegerField(blank=True,null=True)
    age=models.IntegerField(blank=True,null=True)
    service_years=models.IntegerField(blank=True,null=True)
    position=models.CharField(max_length=50)
    user_type=models.IntegerField(null=True,blank=True)
    entry_choices=(('approved','approved'),
                   ('pending','pending'),
                   ('rejected','rejected')
    )
    entry=models.CharField(choices=entry_choices,max_length=50,default='pending')



    def __str__(self):
        return self.username

class Case(models.Model):
    type_choices=(
        ('murder','murder'),
        ('kidnapping','kidnapping'),
        ('damaging property','damaging property'),
        ('rape','rape'),
        ('physical or mental abuse','physical or mental abuse'),
        ('theft','theft'),
        ('others','others')

    )
    type=models.CharField(choices=type_choices,max_length=50)
    date=models.DateField()
    place=models.CharField(max_length=50)
    culprit=models.CharField(max_length=50)
    victim=models.CharField(max_length=50)
    describe=models.CharField(max_length=50)
    user=models.ForeignKey(CustomUser,related_name='my_user',on_delete=models.CASCADE)
    police=models.ForeignKey(CustomUser,related_name='assigned_police',on_delete=models.CASCADE,blank=True)
    status_choices=(('Case ongoing','Case ongoing'),
                    ('Case Incomplete','Case incomplete'),
                    ('Case solved/closed','Case solved/closed')
    )
    status=models.CharField(choices=status_choices,max_length=50)



class Notification(models.Model):
    notification=models.CharField(max_length=300)









