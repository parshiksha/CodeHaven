from django.shortcuts import render
from django.http import HttpResponse

from authen.models import users
# Create your views here.
def index(request):
    print(request.session)
    if "id" in request.session:
        userId = request.session.get('id')
        results = users.objects.filter(id = userId)
        
        

        return render(request, 'codeditor.html', {'name' : results[0].name , 'id' :userId })
        #return HttpResponse("You're loggin")

    else:
        return HttpResponse("You're logged out. Please log in")
    
    
