from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'index.html')

def about(request):
    data='get all data from the database'
    return HttpResponse(data)

def contact(request):
    return HttpResponse('This is our Contact page')
