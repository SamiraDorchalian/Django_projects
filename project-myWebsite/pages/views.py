from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home_page_view(request):
    return render(request, 'home.html')

def about_page_view(request):
    context = {
        'page_name' : 'Main',
        'description' : 'This is something said in context',
        'button_value' : 'Dont Click Me',
    }
    return render(request, 'pages/about.html',context)

def contactus_page_view(request):
    return render(request, 'pages/contactus.html')