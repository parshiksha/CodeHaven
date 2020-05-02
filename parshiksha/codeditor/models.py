from django.db import models
from django.utils.timezone import now, timedelta, datetime

class ProblemInfo(models.Model):
    problemId = models.IntegerField()
    subjectId = models.IntegerField()
    problemText = models.CharField(max_length=200)
    ImageLink = models.CharField(max_length=1000)
    problemSampleInput = models.CharField(max_length=1000)
    problemSampleOutput = models.CharField(max_length=1000)





