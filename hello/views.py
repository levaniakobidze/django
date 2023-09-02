from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request,name):
    age = 21
    
    return render(request,"hello/index.html",{
        "name":name,
        "age": age
    })
