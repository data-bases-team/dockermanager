from users.forms import CustomUserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.shortcuts import render

def dashboard(request):
    return render(request, "dashboard.html")
    
def register(request):
    if request.method == "GET":
        return render(
            request, "register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
# def login(request):
#     return render(request, "login.html")