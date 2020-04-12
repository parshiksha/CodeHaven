from django.db import models

# Create your models here.


class users(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    passoword = models.CharField(max_length=100)
    score = models.IntegerField()
    imageLink = models.CharField(max_length=1000)
    verified = models.BooleanField()
