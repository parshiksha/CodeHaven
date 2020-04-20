from django.shortcuts import redirect, render
from django.utils.timezone import now, timedelta, datetime


from django.http import HttpResponse

from django.contrib.auth.hashers import make_password, check_password
from .models import users, ResetPassword
import uuid
from django.utils import timezone
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from parshiksha.settings import EMAIL_HOST_USER




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def login(request):
    if(request.method == 'POST'):
        email1 = request.POST['email']
        password = request.POST['password']
        print(email1 + password)
        results = users.objects.filter(email=email1)

        if(len(results) > 0):
            if(check_password(password, results[0].passoword)):
                request.session['id'] = results[0].id
                print(results[0].id)

                return redirect('/profile')
            else:
                print("password not correct")
                return render(request, 'login.html', {'message' : 'password or username is not correct, Please try again', 'type': 'alert'})
        else:
            return render(request, 'login.html', {'message' : 'are you sure about your email id?', 'type': 'alert'})

        

        
    else:
        return render(request, 'login.html', {'message' : 'Hey Welcome Again', 'type' : 'info'})


def register(request):
    # return HttpResponse("Regiser form get reust here")
    if(request.method == 'POST'):
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        hashedPassword = make_password(password)
        imageLink = request.POST['imageLink']

        results = users.objects.filter(email=email)
        if(len(results) > 0):
            return HttpResponse("Hey, User already exist from this email id.")
        else:
            x = users(name=name, email=email, passoword=hashedPassword,
                  score=0, imageLink=imageLink, verified=False)
            x.save()
            print("User Createdddddd!!!!!!!!!!!!!!1")
            return render(request, 'login.html', {'message' : 'Hey Welcome to Parshiksha', 'type' : 'info'})

        

        

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
        resetMail = request.POST['email']
        
        resetTokenGG = uuid.uuid4().hex

        link = "http://127.0.0.1:8000/authentication/reset?resetToken="+resetTokenGG
        dbEntry = ResetPassword(email=resetMail, valid= True, resetToken=resetTokenGG,)
        
        #Email setup
        # subject, from_email, to = 'Reset your password - Parshiksha', EMAIL_HOST_USER, resetMail
        # text_content = 'Hey User, You requested to reset your password.'
        # html_content = 'Please go to this link <a href=' + link+'>Link</a> or <p>' + link+' </p>'
        # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        # msg.attach_alternative(html_content, "text/html")
        # msg.send()
        

        print(link)
        dbEntry.save()

        return HttpResponse("Mail sent to : ===>" + resetMail +"and the link is <a href="+ link+">link</a>")
    else:
        return render(request, 'forgot.html')




def reset(request):
    if(request.method == 'POST'):
        userEmail = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if(pass1 == pass2):
            hashedPassword = make_password(pass1)
            passwordUpdate = users.objects.filter(email=userEmail).update(passoword=hashedPassword)
            resetPasswordUpdate = ResetPassword.objects.filter(email=userEmail).update(valid= False)
            
            return HttpResponse("Password reset Success!! for" + userEmail)


    else:
        validatorCode = request.GET['resetToken']        
        resetUser = ResetPassword.objects.filter(resetToken=validatorCode, valid= True)
        if(len(resetUser) > 0):
            email = resetUser[0].email
            if(resetUser[0].expiration > timezone.localtime()):
                return render(request, 'reset.html', {'email' : email})
            else:
                return HttpResponse("Hey your 24 hours of password reset time is over now. Have Fun, Keep learning")
    
        else:
            return HttpResponse("Hey Parshiksha User, you don't have a valid reset token, please reset again to get a new mail")



    
    

