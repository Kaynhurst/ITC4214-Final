from django.db import models

# Create your models here.

class user(models.Model):
    userName = models.CharField(max_length=50,default="JohnDoe")
    userMail = models.EmailField(default="user@mail.com")
    userPassword = models.CharField(max_length=20)
    userAuthority = models.CharField(max_length=15,default="Member")

    def _str_(this):
        return (f"Username : {this.userName} \nUser email : {this.userMail} ")