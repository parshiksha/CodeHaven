from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def index(request):
    demoCode = '1+1+1+1+1+1+1+1'
    return HttpResponse("Welcome to Compiler")


