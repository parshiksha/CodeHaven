
# Create your views here.


# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("This is user profile. fetched data from DB")
    return render(request, 'profile.html')
