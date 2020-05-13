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
    success = models.BooleanField();
    solution = models.CharField(max_length = 20000)
    timeTaken = models.CharField(max_length=20)
    submitTime = models.DateTimeField(auto_now_add=True)






# UserProblemDetails: This table stores the information for each attempt made by a user. 

# UserId: Unique Identifier identifying the user
# ProblemID: Unique Identifier identifying the problem
# TrialCount: The counter associated with the user’s trial number.
# Success: Boolean indicating whether the user succeeded in the attempt or not.
# Solution: Blob indicating the solution that the user gave. Eg. in case of an algorithmic problem this would be a piece of code.
# Time: Overall time it took for the user to submit this solution/answer.












# SubjectInfo: This table stores the information for each subject. 
# SubjectID: Unique Identifier indicating the subject.
# SubjectName: Name of the subject.
# ProblemCount: The number of problems in the subject.


# TestCaseInfo: This table stores the test cases for each of the problems that will be created. 
# TestCaseID: Unique Identifier indicating the test-case.
# ProblemID: Foreign key for the problem (points to the unique id stored in ProblemInfo table).
# SampleInput: Text indicating the sample input to the problem.
# SampleOutput: Text indicating the sample output of the problem.
