
# Create your views here.


# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from authen.models import users


def index(request):
    print(request.session)
    if "id" in request.session:
        userId = request.session['id']
        results = users.objects.filter(id=userId)
        

        return render(request, 'profile.html', {
            'name' : results[0].name,
            'email': results[0].email
        })
    else:
        return HttpResponse("Please log in to see your profile")
