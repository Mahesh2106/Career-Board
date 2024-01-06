from django.db import models

# Create your models here.
class RegistrationDB(models.Model):
    Username=models.CharField(max_length=90,null=True,blank=True)
    Email=models.EmailField(max_length=60,null=True,blank=True,unique=True)
    Password=models.CharField(max_length=60,null=True,blank=True)

