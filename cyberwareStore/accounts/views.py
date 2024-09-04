from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView , DetailView , UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from products.models import *

# Product Manipulation Classes

class EditProductView(UpdateView):
    model = Product
    template_name = "accounts/edit_product.html"
    fields = ['productName', 'productPrice', 'productGrade' , 'productCategory']
    def get_success_url(self):
        return reverse('accounts:profile') 

class AddProductView(CreateView):
    model = Product
    template_name = "accounts/add_product.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse('accounts:profile') 

class DeleteProductView(DeleteView):
    model = Product
    template_name = "accounts/delete_product.html"
    def get_success_url(self):
        return reverse('accounts:profile') 

# User Manipulation Classes
class RegisterView(CreateView):
    form_class= UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/register.html"

class EditUserView(UpdateView):
    model = User
    template_name = "accounts/edit_user.html"
    fields = ['username','password','groups']

    def get_success_url(self):
        return reverse('accounts:profile') 

class DeleteUserView(DeleteView):
    model = User
    template_name = "accounts/delete_user.html"
    def get_success_url(self):
        return reverse('accounts:profile') 


# Create your views here.

@login_required
def profile(request):

    is_Employee = False
    users = User.objects.all

    if (request.user.groups.filter(name='Employee').exists()):
        is_Employee = True

    productsList = Product.objects.all()
    gradeList = Grade.objects.all()
    categoryList = Category.objects.all()

    values = {
            'productsList':productsList ,
            'gradeList':gradeList,
            'categoryList' : categoryList,
            'is_Employee' : is_Employee,
            'users' : users
    }
    
    return render(request,'accounts/profile.html',values)