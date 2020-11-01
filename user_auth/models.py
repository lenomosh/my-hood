from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
# from myHood_Main.models import Hood


class User(AbstractUser):
    hood_name = models.ForeignKey("myHood_Main.Hood", on_delete=models.CASCADE, related_name='residents')

    def __str__(self):
        return self.username

