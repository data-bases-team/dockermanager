from users.forms import CustomUserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.shortcuts import render
import subprocess
from django.http import HttpResponse
import pathlib

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


def run_script(request):
    subprocess.run(["bash", str(pathlib.Path(__file__).parent.parent.resolve()) + "/test.sh"], shell=False)
    return HttpResponse("Script executed successfully")