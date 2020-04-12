from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse

from django.contrib.auth.hashers import make_password, check_password
from .models import users


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def login(request):
    return HttpResponse("Login form")


def register(request):
    # return HttpResponse("Regiser form get reust here")
    if(request.method == 'POST'):
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        hashedPassword = make_password(password)
        imageLink = request.POST['imageLink']
        print(name)
        print(email)
        print(password)
        print(hashedPassword)
        print(imageLink)

        x = users(name=name, email=email, passoword=hashedPassword,
                  score=0, imageLink=imageLink, verified=False)

        x.save()
        print("User Createdddddd!!!!!!!!!!!!!!1")
        return redirect('/profile')

    else:
        return render(request, 'register.html')
