#Home URLS

from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('home/' , views.index , name= "index") 
]