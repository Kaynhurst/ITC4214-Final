from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render
from django import forms
from django.forms import TextInput, EmailInput

class UserLogin(forms.Form) :
    userMail = forms.EmailField(label="E-mail", max_length=20 ,widget=forms.EmailInput(attrs={'class':'form-control border border-success mb-3'}))
    password = forms.CharField(label="Password", max_length=16,widget=forms.PasswordInput(attrs={'class':'form-control border border-success mb-3'}))

class UserRegister(forms.Form) :

    userName = forms.CharField(label="Username", max_length=20 ,widget=forms.TextInput(attrs={'class':'form-control border border-success mb-3'}))
    userMail = forms.EmailField(label="E-mail", max_length=20 ,widget=forms.EmailInput(attrs={'class':'form-control border border-success mb-3'}))
    password = forms.CharField(label="Password", max_length=16,widget=forms.PasswordInput(attrs={'class':'form-control border border-success mb-3'}))

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)

        #Validate User

        if form.is_valid():

            userMail = form.cleaned_data.get('userMail')
            password = form.cleaned_data.get('password')
            user = authenticate(request, userMail=userMail, password=password)
            
            return render(request, 'members/login.html', {
                    'form': form,
                    'username': userMail,
                    'password': password,
                    'show_alert': True,
                    'invalid' : False
                })
        else:
              messages.error(request, 'Invalid username or password.')
              
    return render(request,'members/login.html',{"form" : UserLogin()})

def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
    
    return render(request,'members/registration.html',{"form" : UserRegister})

def profile(request,name):
    return render(request,'members/profile.html',{'name':name})