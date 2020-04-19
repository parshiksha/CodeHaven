from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print(request.session)
    if "id" in request.session:
        return render(request, 'codeditor.html')
    else:
        return HttpResponse("You're logged out. Please log in")
    
    
