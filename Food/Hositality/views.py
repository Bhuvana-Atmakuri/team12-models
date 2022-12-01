from operator import itemgetter
from django.http import HttpResponse
from django.http import HttpResponse
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
from .tokens import Generate_Token
from django.shortcuts import render, redirect
from .models import Hotels, items


def home(request):
    allnoes = Hotels.objects.all()
    cate = list(Hotels.objects.values_list('catego', flat=True).distinct())
    return render(request, "hello.html", {'no': allnoes, 'cat': cate})


def id(request, store_id):
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
    return render(request,"preorder.html")

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

        return redirect("pre")
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