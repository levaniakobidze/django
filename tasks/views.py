from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    tasks = ['make dinner', 'study english' , 'workout' ]
    return render(request,'tasks/index.html',{
        "todos": tasks
    })



def add(request):
    print(request)
    return render(request,'tasks/add.html')

