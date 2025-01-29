from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def show_pizza(request):
    return HttpResponse("""
    <h1>Hello this is my page</h1>
    <input type="button" value="click me" />
    """)

def show_hamburger(request):
    return HttpResponse('Hamburger')

def show_rice_chicken(request):
    return HttpResponse('Iran')

def home_view(request):
    return HttpResponse('Home of Food')