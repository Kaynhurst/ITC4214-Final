from django.db import models

# Create your models here.

class Category (models.Model):
    categoryName = models.CharField(max_length=50)
    
    def __str__(self):
        return (f"Category ID : {self.id} + Category Name : {self.categoryName}")
    

class Grade (models.Model):
    gradeName = models.CharField(max_length=50)

    def __str__(self):
        return (f"Grade ID : {self.id} + Grade Name : {self.gradeName}")
    

class Product(models.Model):
    productName = models.CharField(max_length=50)
    productPrice = models.FloatField()
    productGrade = models.ForeignKey(Grade,on_delete=models.CASCADE)
    productCategory = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return (f"Product ID : {self.id} + Product Name : {self.productName} + Price : {self.productPrice} + Grade : {self.productGrade.gradeName} + Category : {self.productCategory.categoryName}")
    

class CheckoutCart (models.Model):
    item = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return (f"Product Name : {self.item.productName} + Product Price : {self.item.productPrice}")