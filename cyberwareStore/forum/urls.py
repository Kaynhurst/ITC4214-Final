#Forum URLS

from django.urls import path
from . import views

urlpatterns = [
    path('forum/' , views.index , name = "index")
]