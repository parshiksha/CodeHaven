from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

from authen.models import users
# Create your views here.
def index(request):
    print(request.session)
    if "id" in request.session:
        userId = request.session.get('id')
        results = users.objects.filter(id = userId)
        print(results)
        
        

        return render(request, 'codeditor.html')
        #return HttpResponse("You're loggin")

    else:
        return render(request, 'codeditor.html')
    
    

def compile(request):

    return HttpResponse("Im about to compile")