from django.shortcuts import render
from django.http import HttpResponse 
from  datetime import datetime

# Create your views here.

def Display(request):
    s = '<h1> Hello welcome to the royal Tea shop</h1>'
    return HttpResponse(s)

def Goodmorning_views(request):
    s = '<h1> Hello friends Good Morning</h1>'
    return HttpResponse(s)

def Goodafternoon_views(request):
    s = '<h1> Hello friends Good Afternoon</h1>'
    return HttpResponse(s)

def Goodevening_views(request):
    s = '<h1> Hello friends Good Evening</h1>'
    return HttpResponse(s) 

def time_info_view(request): 
    time=datetime.now() 
    s='<h1>Hello Current Date and Time is :'+str(time)+'</h1>' 
    return HttpResponse(s) 
