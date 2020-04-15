from django.db import models

class SubjectInfo(models.model):
    subjectId=models.AutoField(primary_key=True)
    subjectName=models.CharField(max_length=30)
    problemCount=models.PositiveIntegerField()

class ProblemInfo(models.Model):
    problemId=models.AutoField(primary_key=True)
    subjectId=models.models.ForeignKey(SubjectInfo, on_delete=models.CASCADE)
    problemText=models.TextField()
    imageLink=models.TextField()

class TestCaseInfo(models.Model):
    testCaseId=models.AutoField(primary_key=True)
    problemId=models.ForeignKey(ProblemInfo, on_delete=models.CASCADE)
    sampleInput=models.TextField()
    sampleOutput=models.TextField()

class UserProblemDetails(models.Model):
    userId=models.PositiveIntegerField() # This should be a foreign-key.
    problemId=models.ForeignKey(ProblemInfo, on_delete=models.CASCADE)
    trialCount=models.PositiveIntegerField()
    success=models.BooleanField(default=False)
    solution=models.TextField()
    time_sec=models.PositiveIntegerField()