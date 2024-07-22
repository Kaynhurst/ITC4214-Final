#Member URLS

from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('login/' , views.login , name ="login"),
    path('register/',views.register, name ="register"),
    path('profile/',views.profile,name="profile")
]