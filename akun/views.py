from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *

def logout_view(request):
    logout(request)
    return redirect("akun:login")

def login_view(request):
    if request.user.is_authenticated:
        return redirect("pengeluaran:landing_page")
    
    form = FormLogin(request.POST or None)

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("pengeluaran:landing_page")
        else:
            messages.error(request, "Username atau Password salah.")

    context = {
        "form": form
    }
    return render(request, "akun/login.html", context)
