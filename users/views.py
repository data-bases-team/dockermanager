from users.forms import CustomUserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.shortcuts import render
import subprocess
from django.http import HttpResponse
import pathlib
from .forms import ContainerForm
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from .models import container
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def add_container(request):
    submitted = False
    if request.method == "POST":
        form = ContainerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add?submitted=True')
    else:
        form = ContainerForm
        if 'submitted' in request.GET:
            submitted=True
            return redirect(reverse("dashboard"))
    return render(request, 'add_container.html', {'form':form, 'submitted':submitted})

@login_required(login_url='/accounts/login/')
def delete_container(request, container_name):
    print(container_name)
    container.objects.get(name=container_name).delete()
    return redirect(reverse("dashboard"))

@login_required(login_url='/accounts/login/')
def restatus_container(request, container_name):
    cont = container.objects.get(name=container_name)
    if cont.status == 'e':
        cont.status = 'd'
    else:
        cont.status = 'e'
    cont.save()
    return redirect(dashboard)

@login_required(login_url='/accounts/login/')
def prolong_container(request, container_name):
    cont = container.objects.get(name=container_name)
    cont.expdate=datetime.now() + timedelta(minutes = 10)
    cont.status = 'e'
    cont.save()
    return redirect(dashboard)

@login_required(login_url='/accounts/login/')
def dashboard(request):
    containers = container.objects.filter(userid=request.user)
    return render(request, "dashboard.html", {'containeros':containers})
    
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

