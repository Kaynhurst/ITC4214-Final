from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'members/login.html',{})

def register(request):
    return render(request,'members/registration.html',{})