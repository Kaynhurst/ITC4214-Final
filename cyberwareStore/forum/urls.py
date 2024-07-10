#Forum URLS

from django.urls import path
from . import views

app_name= 'forum'
urlpatterns = [
    path('forum/' , views.index , name = "index")
]