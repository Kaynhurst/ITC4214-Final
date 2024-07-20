from django.contrib import admin
from .models import *

# Register your models here.
class productAdmin(admin.ModelAdmin):
    readonly_fields=('id',)

admin.site.register(Grade)
admin.site.register(Category)
admin.site.register(Product,productAdmin)
admin.site.register(CheckoutCart)