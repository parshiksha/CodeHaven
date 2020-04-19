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
            request.session['id'] = results[0].id
            print(results[0].id)

            # payload = jwt_payload_handler(user)
            # token = jwt.encode(payload, settings.SECRET_KEY)
            # user_details = {}
            # user_details['name'] = "%s %s" % (results[0].name, email1)
            # user_details['token'] = token

            #print(user_details)
            # user_logged_in.send(sender=user.__class__, request=request, user=user)
            # return Response(user_details, status=status.HTTP_200_OK)
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


def logout(request):
    try:
        del request.session['id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")



def forgot(request):
    if(request.method == 'POST'):
        link = "http://127.0.0.1:8000/authentication/reset?resetToken=qwertyuiop"
        resetMail = request.POST['email']
        return HttpResponse("Mail sent to : ===>" + resetMail)
    else:
        return render(request, 'forgot.html')



def reset(request):
    if(request.method == 'POST'):
        userEmail = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if(pass1 == pass2):
            #update password in DB here
            return HttpResponse("Password reset Success!! for" + userEmail)


    else:
        validatorCode = request.GET['resetToken']


        emailOfUser = 'sidsaini1196@gmail.com' #get email from this validation code.
        return render(request, 'reset.html', {
            'email' : emailOfUser
        })


    
    

