from django.shortcuts import render,redirect
from .forms import UserRegisterForm,LoginForm
from django.contrib.auth import authenticate, login, logout 


# Create your views here.

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            userName = form.cleaned_data['userName']
            userPassword = form.cleaned_data['password']
            user = authenticate(request, username=userName, userPassword=userPassword)
            if user:
                login(request, user)    
                return redirect('home/index.html')
    else:
        form = LoginForm()
    return render(request, 'members/login.html', {'form': form})

def register(request):

    if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('members/login.html')
    else:
        form = UserRegisterForm()

    return render(request,'members/registration.html',{"form" : form})

def profile(request):
        
    username = None
    values ={
        'username':username
        }
    return render(request,'members/profile.html',values)

def user_logout(request):
    logout(request)
    return redirect('members/login.html')
