#Product URLS

from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('products/' , views.index , name="index")
]