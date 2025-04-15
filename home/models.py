from django.db import models

# Create your models here.

class booktable(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Time = models.CharField(max_length=50)
    Date = models.CharField(max_length=50)

class signupdetails(models.Model):
    Email = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)