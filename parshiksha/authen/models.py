from django.db import models
from django.utils.timezone import now, timedelta, datetime


# Create your models here.
def s_tomorrow():
    return datetime.now() + timedelta(days=1)

class users(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    passoword = models.CharField(max_length=100)
    score = models.IntegerField()
    imageLink = models.CharField(max_length=1000)
    verified = models.BooleanField()


class ResetPassword(models.Model):
    email = models.CharField(max_length=100)
    resetToken = models.CharField(max_length=200)
    valid = models.BooleanField()
    created = models.DateTimeField(default=now)
    expiration = models.DateTimeField(default = s_tomorrow)



