from django.db import models

# Create your models here.
class ContactDb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100)
    Message = models.TextField()

class RegistrationDb(models.Model):
    UserName = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(null=True,blank=True)
    Password = models.CharField(max_length=100,null=True,blank=True)
    Confirm_Password = models.CharField(max_length=100,null=True,blank=True)