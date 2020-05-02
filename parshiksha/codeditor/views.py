from django.shortcuts import render
from django.http import HttpResponse


from authen.models import users
# Create your views here.
def index(request):
    print(request.session)
    if "id" in request.session:
        userId = request.session.get('id')
        results = users.objects.filter(id = userId)
        
        

        return render(request, 'codeditor.html')
        #return HttpResponse("You're loggin")

    else:
        return render(request, 'codeditor.html')
    
    
