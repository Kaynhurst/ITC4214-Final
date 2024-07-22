from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    userName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control border border-success mb-3'}))
    password = forms.CharField(label="Password", max_length=16,widget=forms.PasswordInput(attrs={'class':'form-control border border-success mb-3'}))