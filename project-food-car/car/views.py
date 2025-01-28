from django.shortcuts import render
from django.http import HttpResponse

def show_mwm(request):
    return HttpResponse('I am MWM')

def show_pars(request):
    return HttpResponse('I am PARS')

def show_home(request):
    return HttpResponse('THIS IS HOME!')