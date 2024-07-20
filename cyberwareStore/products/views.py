from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    productsList = Product.objects.all()
    gradeList = Grade.objects.all()
    categoryList = Category.objects.all()

    cart = CheckoutCart.objects.all()
    sum = cart.count()
    if productsList is not None :
        return render(request,'products/index.html',{'productsList':productsList , 'gradeList':gradeList, 'categoryList' : categoryList,'total' : sum})
    
def cart(request):

    return render(request,'products/cart.html',)

def addProduct(request):

    return render(request,'products/cart.html')
