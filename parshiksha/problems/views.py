from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import ProblemInfo, SubjectInfo, TestCaseInfo, UserProblemDeatils
from authen.models import users
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json



# Create your views here.
def index(request):
    problems = list(ProblemInfo.objects.filter())
    #print(problems[0].problemTitle)
    #print(type(problems))
    problems_json = serializers.serialize('json', problems)
    return HttpResponse(problems_json, content_type='application/json')

    #return JsonResponse(problems,safe=True)
    
    

    
def getSubjects(request):
    subjects = list(SubjectInfo.objects.filter())
    subjects_json = serializers.serialize('json', subjects)
    return HttpResponse(subjects_json, content_type='application/json')

@csrf_exempt
def getTestCaseInfo(request):
    if(request.method == 'POST'):
        decodedData = request.body.decode('utf-8')
        body = json.loads(decodedData)
        problemIdFromUser = body['problemId']

        print(problemIdFromUser)
        testCaseDeatil = list(TestCaseInfo.objects.filter(problemId = problemIdFromUser))

        if(len(testCaseDeatil) > 0):
            testcaseinfo_json = serializers.serialize('json', testCaseDeatil)
            return HttpResponse(testcaseinfo_json, content_type='application/json')
            
        else:
            return HttpResponse("SHit :(, Code Fatt gya!")
        #return HttpResponse("getting provlem ID")
   
    else:
        return HttpResponse("Dude! this is post request")




@csrf_exempt
def submitAnswer(request):
    if(request.method == 'POST'):
        decodedData = request.body.decode('utf-8')
        body = json.loads(decodedData)

        userId = body['userId']
        problemId= body['problemId']
        trailCount = body['trailCount']
        success = body['success']
        solution = body['solution']
        timeTaken = body['timeTaken']
        user = users.objects.get(id = userId)
        problem = ProblemInfo.objects.get(problemId = problemId)
        
        submission  = UserProblemDeatils(userId=user,problemId=problem,trailCount=trailCount, 
        success=success,  solution=solution,  timeTaken= timeTaken )

        submission.save()
        print("Solution Submission Success!!!!!!!!")
        return HttpResponse("Wow! wowowowwo")
    else:
        return HttpResponse("Dude! this is post request")
        














