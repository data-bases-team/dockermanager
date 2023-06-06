from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group, User
from .models import container

admin.site.register(container)