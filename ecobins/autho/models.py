from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

usermodel=get_user_model()

class Userauth(models.Model):
    user = models.OneToOneField(usermodel,on_delete=models.CASCADE)
    phone = models.CharField(max_length=15,blank=False)

    name = models.CharField(max_length=50,blank=False)
    age = models.PositiveBigIntegerField(blank=False)
    address = models.TextField(blank=False)