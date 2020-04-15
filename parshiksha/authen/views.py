from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse

from django.contrib.auth.hashers import make_password, check_password
from .models import users


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def login(request):
    if(request.method == 'POST'):
        email1 = request.POST['email']
        password = request.POST['password']
        print(email1 + password)
        results = users.objects.filter(email=email1)
        # print(results[0].name)

        if(check_password(password, results[0].passoword)):
            return redirect('/profile')
        else:
            print("password not correct")
    else:
        return render(request, 'login.html')


def register(request):
    # return HttpResponse("Regiser form get reust here")
    if(request.method == 'POST'):
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        hashedPassword = make_password(password)
        imageLink = request.POST['imageLink']

        x = users(name=name, email=email, passoword=hashedPassword,
                  score=0, imageLink=imageLink, verified=False)

        x.save()
        print("User Createdddddd!!!!!!!!!!!!!!1")
        return redirect('/profile')

    else:
        return render(request, 'register.html')
