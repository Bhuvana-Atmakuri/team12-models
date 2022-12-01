from django.db import models
from django.contrib.auth import get_user_model


class Hotels(models.Model):
    hotelname=models.CharField(max_length=100,default="")
    id= models.BigAutoField(primary_key=True)
    catego=models.CharField(max_length=200,default="")
    image=models.ImageField(upload_to ='documents/')
    timi = models.CharField(max_length=100, default="")
    tagline = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=200, default="")

    def str(self):
        return self.hotelname


class items(models.Model):
    artist = models.ForeignKey(Hotels, on_delete=models.CASCADE,null=True)
    hotelname1=models.CharField(max_length=100)
    category=models.CharField(max_length=200)
    item1=models.ImageField(upload_to='documents/')
    ititle=models.CharField(max_length=100)
    iprice=models.CharField(max_length=100)
    def str(self):
        return self.hotelname1


User=get_user_model()
class Customer(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.TextField()
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()