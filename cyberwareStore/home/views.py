from django.shortcuts import render
from products.models import *

# Create your views here.

def index(request):
    cart = CheckoutCart.objects.all()

    sum = 0
    for item in cart :
        sum += 1

    return render(request,'home/index.html',{'total' : sum})