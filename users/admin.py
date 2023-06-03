from django.contrib import admin
from .models import container
from django.utils.html import format_html
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group, User


admin.site.register(container)
