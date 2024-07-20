#Product URLS

from django.urls import path
from products import views


app_name = 'products'

urlpatterns = [
    path('products/' , views.index , name="index"),
    path('cart/' , views.cart , name = "cart"),
    path('add_product',views.addProduct, name="add_product"),
]
