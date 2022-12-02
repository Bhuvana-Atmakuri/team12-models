from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import uuid


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
    modelid=models.IntegerField(blank=True, null=True)
    def str(self):
        return self.hotelname1


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(items,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity*self.product.iprice

class Dinein(models.Model):
    hname=models.CharField(max_length=200)
    Description=models.CharField(max_length=500)
    img=models.ImageField(upload_to='documents/')
    category=models.CharField(max_length=100)
    location=models.CharField(max_length=150)
    Timings=models.CharField(max_length=100)
    id = models.BigAutoField(primary_key=True)
    iprice = models.CharField(max_length=100)
    def str(self):
        return self.hname

class dine1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Dinein, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.iprice

STATUS_CHOICES={

    ('Accepted','Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel','Cancel'),
    ('Pending', 'Pending'),
}

class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.FloatField()
    razorpay_order_id=models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    paid=models.BooleanField(default=False)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(items, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE)
    @property
    def total_cost(self):
        return self.quantity*self.product.iprice



