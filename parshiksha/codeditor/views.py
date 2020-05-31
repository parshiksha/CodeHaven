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

    post_data = {
   "script" : "console.log('hello')",
   "language": "nodejs",
   "versionIndex": "1",
   "clientId": "b43fad100c8478b5e26b2d6aab5c46ff",
   "clientSecret": "105b800cd9390f38f7fd8cd4cf4e02348583b8d816f582f859e5f6e6175ea7f3"
}

    response = requests.post('https://api.jdoodle.com/execute', data=json.dumps(post_data))
    print(response)
    return HttpResponse(response)