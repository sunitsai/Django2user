from django.db import models

# Create your models here.
class User(models.Model):
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    otp = models.IntegerField()
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now=True,blank=False)
    is_active = models.BooleanField(default=True)
    is_update = models.DateTimeField(auto_now_add=True,blank=False)

class Employee(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    contact = models.BigIntegerField(default=1)
    # pics = models.ImageField(upload_to="img/")
