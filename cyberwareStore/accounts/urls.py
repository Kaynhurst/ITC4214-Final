from django.urls import path
from . import views
from .views import *

app_name = "accounts"

urlpatterns =[
    path("register/",RegisterView.as_view(), name = "signup"),
    path('profile/' , views.profile , name = "profile"),
    path("addproduct/" , AddProductView.as_view(), name="addProduct") ,
    path("editproduct/<int:pk> ", EditProductView.as_view(), name="editProduct"),
    path("deleteproduct/<int:pk>" , DeleteProductView.as_view(), name="deleteProduct"),
    path("edituser/<int:pk>" , EditUserView.as_view(), name="editUser"),
    path("deleteuser/<int:pk>" , DeleteUserView.as_view(), name="deleteUser")
]