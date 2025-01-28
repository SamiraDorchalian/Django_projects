from django.shortcuts import render
from  django.http import HttpResponse


# Create your views here.
def say_something(request):
    return HttpResponse('Hello Bye')