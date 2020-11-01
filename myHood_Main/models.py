from django.contrib.auth.models import AbstractUser
from django.db import models
from user_auth.models import User


# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Hood(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='hoods')
    admin = models.OneToOneField(User,on_delete=models.SET_NULL, related_name='hood',null=True)

    def __str__(self):
        return self.name


class Business(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='business')
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, related_name='businesses')
    email = models.EmailField()

    def __str__(self):
        return self.name

