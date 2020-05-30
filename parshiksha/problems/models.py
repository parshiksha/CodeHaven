from django.db import models

from authen.models import users

import datetime

# Create your models here.
class ProblemInfo(models.Model):
    problemId = models.AutoField(primary_key=True)
    subjectID = models.IntegerField()
    problemTitle = models.CharField(max_length=500)
    problemText = models.CharField(max_length=2000)
    imageLink = models.CharField(max_length=1000)
    sampleDummyInput = models.CharField(max_length=500)
    sampleDummyOutput = models.CharField(max_length=500)


class TestCaseInfo(models.Model):
    testCaseId = models.AutoField(primary_key=True)
    problemId = models.ForeignKey(ProblemInfo, on_delete=models.CASCADE)
    sampleInput = models.CharField(max_length=500)
    sampleOutput = models.CharField(max_length=500)


class SubjectInfo(models.Model):
    subjectId = models.AutoField(primary_key=True)
    subjectName = models.CharField(max_length=100)
    problemCount = models.IntegerField()

class UserProblemDeatils(models.Model):
    userId = models.ForeignKey(users, on_delete=models.CASCADE)
    problemId = problemId = models.ForeignKey(ProblemInfo, on_delete=models.CASCADE)
    trailCount = models.IntegerField()
    success = models.BooleanField()
    solution = models.CharField(max_length = 20000)
    timeTaken = models.CharField(max_length=20)
    submitTime = models.DateTimeField(auto_now_add=True)

