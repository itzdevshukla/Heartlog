from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def register(request):
    if request.method == "POST":
        user_first_name = request.POST.get("first_name")
        user_last_name = request.POST.get("last_name")
        user_username = request.POST.get("username")
        user_email = request.POST.get("email")
        user_password = request.POST.get("password")

        new_user = User(
            username = user_username,
            first_name = user_first_name,
            last_name = user_last_name,
            email = user_email
        )
        new_user.set_password(user_password)
        new_user.save()
        return redirect("login")

    return render(request,"accounts/register.html")
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request,username=username ,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("register")
    return render(request,"accounts/login.html")

def logout(request):
    auth.logout(request)
    return redirect("home")