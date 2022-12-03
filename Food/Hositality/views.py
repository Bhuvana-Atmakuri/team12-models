from operator import itemgetter


from django.db.models import Q
from django.http import HttpResponse
from django.http import HttpResponse
import razorpay
from email.message import EmailMessage
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from razorpay.resources import payment

from .tokens import Generate_Token
from django.shortcuts import render, redirect
from .models import *

from django.http import JsonResponse
import json
from django.contrib import messages





def home(request):
    user=request.user
    allnoes = Hotels.objects.all()
    cate = list(Hotels.objects.values_list('catego', flat=True).distinct())
    cart = Cart.objects.filter(user=user)
    amount = 0
    q = 0
    shipping = 40
    for p in cart:
        k = int(p.product.iprice)
        q = q + p.quantity
        value = p.quantity * k
        amount = amount + value
    totalamount = amount + 40
    return render(request, "hello.html", {'no': allnoes, 'cat': cate,'q':q})





def id(request, store_id):
    user=request.user
    k=[]
    machine = Hotels.objects.get(id=store_id)
    hoti=items.objects.filter(hotelname1=machine.hotelname)
    #for item in hoti:
       # print(item.hotelname1)
        #print(item.category)

    for h in hoti:
        k.append(h.category)
    #print(k)
    inn = items.objects.all()
    #inn1=items.objects.get(iprice=30)
    hote = list(items.objects.values_list('category', flat=True).distinct())

    return render(request, "order.html", {'inn': inn, 'hot': hote, 'si': store_id, 'ma': machine, 'k':k})




def pre(request):
    user = request.user
    allnoes = Hotels.objects.all()
    cate = list(Hotels.objects.values_list('catego', flat=True).distinct())
    cart = Cart.objects.filter(user=user)
    amount = 0
    q = 0
    shipping = 40
    for p in cart:
        k = int(p.product.iprice)
        q = q + p.quantity
        value = p.quantity * k
        amount = amount + value
    totalamount = amount + 40

    user = request.user
    alldine = Dinein.objects.all()
    cate = list(Dinein.objects.values_list('category', flat=True).distinct())
    cart = dine1.objects.filter(user=user)
    amount = 0
    qua = 0
    for p in cart:
        k = int(p.product.iprice)
        qua = qua + p.quantity
        value = p.quantity * k
        amount = amount + value
    totalamount = amount
    return render(request,"preorder.html",locals())



def log(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        myuser = User.objects.create_user(username, email, password)


        if not username.isalnum():
            messages.error(request, "User name must be alpha numeric")

        myuser.save()
        messages.success(request,
                         "Your account has been successfully created we have sent you a confirmation email!please confirm your email to activate your account")

        subject = "Welcome to Aaharam"
        message = "Hello!" + myuser.username + "! \n\n" + "Welcome to Aaharam!\n\nThankyou for registering for our website \n\n we have also sent you a confirmation email ,please confirm your email address in order to activate your account\n\n" + "Thanking you\n\n Bhuvana"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        current_site = get_current_site(request)
        email_subject = "Confirm your email for Aaharam website"
        message2 = render_to_string('email_confimation.html', {
            'name': myuser.username,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': Generate_Token.make_token(myuser)

        })
        email = EmailMessage(email_subject, message2, settings.EMAIL_HOST_USER, [myuser.email], )
        email.fail_silently = True
        email.send()

        return redirect("sign")
    return render(request, "signup.html")



def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and Generate_Token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        # login(myuser,request)
        return redirect("pre")
    else:
        return render(request, 'activation_failed.html')


def sign(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in succesfully")
            return render(request, "preorder.html", {})
        else:
            k="Invalid Credentials Try Again"
            return render(request,"login.html",{'k':k})
    return render(request,"login.html")




def login1(request):
    return render(request,"signup.html")



def addto(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product=items.objects.get(modelid=product_id)
    Cart(user=user,product=product).save()
    return redirect('cart')




def cart(request):
    user=request.user
    cart=Cart.objects.filter(user=user)
    amount=0
    q=0
    shipping=40
    for p in cart:
        k=int(p.product.iprice)
        q=q+p.quantity
        value=p.quantity*k
        amount=amount+value
    totalamount=amount+40
    return render(request,'addtocart.html',locals())




def plus_cart(request,product_id):
    if(product_id<10):
       c = Cart.objects.get(product=product_id+2)
       c.quantity += 1
       c.save()
       user = request.user
       cart = Cart.objects.filter(user=user)
       amount = 0
       q = 0
       for p in cart:
           k = int(p.product.iprice)
           q = q + p.quantity
           value = p.quantity * k
           amount = amount + value
       totalamount = amount + 40
       return redirect('cart')
    else:
            c = Cart.objects.get(product=product_id + 3)
            c.quantity += 1
            c.save()
            user = request.user
            cart = Cart.objects.filter(user=user)
            amount = 0
            q = 0
            for p in cart:
                k = int(p.product.iprice)
                q = q + p.quantity
                value = p.quantity * k
                amount = amount + value
            totalamount = amount + 40
            return redirect('cart')




def minus_cart(request,product_id):
    shipping = 0
    if (product_id < 10):
        c = Cart.objects.get(product=product_id + 2)
        c.quantity -= 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        q = 0
        for p in cart:
            k = int(p.product.iprice)
            q = q + p.quantity
            value = p.quantity * k
            amount = amount + value
        totalamount = amount + 40
        return redirect('cart')
    else:
        c = Cart.objects.get(product=product_id + 3)
        c.quantity -= 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        q = 0
        for p in cart:
            k = int(p.product.iprice)
            q = q + p.quantity
            value = p.quantity * k
            amount = amount + value
        totalamount = amount + 40
        return redirect('cart')



def remove_cart(request,remove_id):
   if(remove_id<10):
      card = Cart.objects.get(product=remove_id+2)
      card.delete()
      return redirect("cart")
   else:
         card = Cart.objects.get(product=remove_id + 3)
         card.delete()
         return redirect("cart")



def removeall(request):
    card = Cart.objects.all()
    card.delete()
    return redirect("cart")


def dine(request):
    user = request.user
    alldine = Dinein.objects.all()
    cate = list(Dinein.objects.values_list('category', flat=True).distinct())
    cart = dine1.objects.filter(user=user)
    amount = 0
    q = 0
    for p in cart:
        k = int(p.product.iprice)
        q = q + p.quantity
        value = p.quantity * k
        amount = amount + value
    totalamount = amount
    return render(request, "dine.html", locals())

def dineto(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product=Dinein.objects.get(id=product_id)
    dine1(user=user,product=product).save()
    return redirect('dinein')

def dinein(request):
    user = request.user
    cart = dine1.objects.filter(user=user)
    amount = 0
    q = 0
    for p in cart:
        k = int(p.product.iprice)
        q = q + p.quantity
        value = p.quantity * k
        amount = amount + value
    totalamount = amount
    return render(request, 'dinein.html', locals())

def plus_cartd(request,product_id):
    c = dine1.objects.get(product=product_id)
    c.quantity += 1
    c.save()
    user = request.user
    cart = dine1.objects.filter(user=user)
    amount = 0
    q = 0
    for p in cart:
        k = int(p.product.iprice)
        q = q + p.quantity
        value = p.quantity * k
        amount = amount + value
    totalamount = amount

    data = {

        'amount': amount,
        'totalamount': totalamount

    }

    return redirect('dinein')




def minus_cartd(request,product_id):
    shipping = 0
    c = dine1.objects.get(product=product_id)
    if(c.quantity>0):
        c.quantity -= 1
        c.save()
        user = request.user
        cart = dine1.objects.filter(user=user)
        amount = 0
        q = 0

        for p in cart:
              k = int(p.product.iprice)
              q = q + p.quantity
              value = p.quantity * k
              amount = amount + value
        totalamount = amount + 40
        return redirect('dinein')
    else:
        return redirect('dinein')




def remove_cartd(request,remove_id):

    card = dine1.objects.get(product=remove_id)
    card.delete()
    return redirect("dinein")



def removealld(request):
    card = dine1.objects.all()
    card.delete()
    return redirect("dinein")

def checkout(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    q = 0
    shipping = 40
    for p in cart:
        k = int(p.product.iprice)
        q = q + p.quantity
        value = p.quantity * k
        amount = amount + value
    totalamount = amount + 40
    razoramount=int(totalamount*100)
    client = razorpay.Client(auth=(settings.RAZOR_KEY_ID,settings.RAZOR_KEY_SECRET))
    data={"amount":razoramount,"currency":"INR","receipt":"order_rcptid_16"}
    payment_response=client.order.create(data=data)
    print(payment_response)
    order_id = payment_response['id']
    order_status = payment_response['status']
    if order_status == 'created':
        payment=Payment(
            user=user,
            amount=totalamount,
            razorpay_order_id=order_id,
            razorpay_payment_status=order_status,
        )
        payment.paid = True
        payment.save()
    return render(request,"checkout.html",locals())


def paymentdone(request):
    payment_id = request.GET.get('payment_id')
    order_id = request.GET.get('order_id')
    print(order_id)
    cust_id = request.GET.get('cust_id')
    user=request.user
    k="Your payment is successfull"
    razorpay_payment_id = payment_id
    p = Payment.objects.all()
    return render(request, "productpayment.html", locals())

def dineinch(request):
    user = request.user
    cart = dine1.objects.filter(user=user)
    amount = 0
    q = 0
    shipping = 40
    for p in cart:
        k = int(p.product.iprice)
        q = q + p.quantity
        value = p.quantity * k
        amount = amount + value
    totalamount = amount + 20
    razoramount=int(totalamount*100)
    client = razorpay.Client(auth=(settings.RAZOR_KEY_ID,settings.RAZOR_KEY_SECRET))
    data={"amount":razoramount,"currency":"INR","receipt":"order_rcptid_16"}
    payment_response=client.order.create(data=data)
    print(payment_response)
    order_id = payment_response['id']
    order_status = payment_response['status']
    if order_status == 'created':
        payment=Payment(
            user=user,
            amount=totalamount,
            razorpay_order_id=order_id,
            razorpay_payment_status=order_status,
        )
        payment.paid = True
        payment.save()
    return render(request,"dineincheckout.html",locals())

def paymentdone1(request):
    payment_id = request.GET.get('payment_id')
    order_id = request.GET.get('order_id')
    print(order_id)
    cust_id = request.GET.get('cust_id')
    user=request.user
    k="Your payment is successfull"
    razorpay_payment_id=payment_id
    return render(request,"addtocart.html",{"message":k})
def aboutus(request):
    return render(request,'aboutus.html')

def pr(request):
    p = Payment.objects.all()
    return render(request,'productpayment.html',locals())