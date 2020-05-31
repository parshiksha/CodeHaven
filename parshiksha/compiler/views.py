from django.shortcuts import render
from django.http import HttpResponse
import parso


# Create your views here.
def index(request):
    demoCode = '1+1+1+1+1+1+1+1'
    module = parso.parse(demoCode, version="3.6")
    #print(module)
    expr = module.children[0]
    print(expr.get_code())
    f= open("codeGG.py","w+")
    print('File created')
    f.write(expr.get_code())
    f.close() 


    return HttpResponse("Welcome to Compiler")


