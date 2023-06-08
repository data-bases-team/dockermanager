from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import container


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

class ContainerForm(ModelForm):
    class Meta:
        model = container
        fields = ('name', 'login', 'password')