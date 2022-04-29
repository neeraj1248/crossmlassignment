import imp
from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Card
from crossmlassignment.choice import *
from django.contrib.auth.models import User

# Create your views here.


# login function with GET and POST request...
def login(request):
    ctx={}
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get("username",None)
            password = request.POST.get("password",None)
            if username and password:
                user_obj = authenticate(request, username=username, password=password)
                if user_obj is not None:
                    auth_login(request, user_obj)
                    return redirect('home')
                else:
                    ctx['error'] = "Username and Password Incorrect"
                    return render(request,'login.html',ctx)
            else:
                return render(request,'login.html')
        else:
            return render(request,'login.html',ctx)


# render Dashboard page with GET request , Home page
@login_required(login_url='/login')
def home(request):
    ctx={}
    card_obj = Card.objects.all().order_by("-id")
    ctx['card_obj']=card_obj

    type = Type.CHOICES
    ctx['type'] = type

    priority = Priority.CHOICES
    ctx['priority'] = priority

    status = Status.CHOICES
    ctx['status'] = status

    user_obj = User.objects.all()
    ctx['user_obj']=user_obj

    return render(request,'dashboard.html',ctx)


# Save the card data with post request...
@login_required(login_url='/login')
def add_card_data(request):
    if request.method=="POST":
        type = request.POST.get("type",None)
        status = request.POST.get("status",None)
        priority = request.POST.get("priority",None)
        assignee_user = request.POST.get("user",None)

        if type and status and priority and assignee_user:
            x = Card(
                type = type,
                priority = priority,
                status = status,
                assignee_id = assignee_user
            )
            x.save()
    return redirect('home')


#Logout function
def logout(request):
    from django.contrib import auth
    auth.logout(request)
    return redirect('/login')
