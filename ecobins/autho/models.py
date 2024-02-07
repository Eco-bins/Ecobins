from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

usermodel=get_user_model()

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=255)
    Email = models.EmailField(default='example@gmail.com')
    Phone = models.CharField(max_length=15)
    Password = models.CharField(max_length=255,default='ertyuiop')
