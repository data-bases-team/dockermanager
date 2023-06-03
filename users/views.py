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


def run_script_start(request):
    subprocess.run(["bash", str(pathlib.Path(__file__).parent.parent.resolve()) + "/start.sh"], shell=False)
    return HttpResponse("Script executed successfully")

def run_script_end(request):
    subprocess.run(["bash", str(pathlib.Path(__file__).parent.parent.resolve()) + "/end.sh"], shell=False)
    return HttpResponse("Script executed successfully")

def run_script_prolong(request):
    subprocess.run(["bash", str(pathlib.Path(__file__).parent.parent.resolve()) + "/prolong.sh"], shell=False)
    return HttpResponse("Script executed successfully")