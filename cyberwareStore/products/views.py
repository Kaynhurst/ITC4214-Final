from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    productsList = Product.objects.all()
    gradeList = Grade.objects.all()
    categoryList = Category.objects.all()
    return render(request,'products/index.html',{'productsList':productsList , 'gradeList':gradeList, 'categoryList' : categoryList})

def cart(request):
    

    return render(request,'products/cart.html',)