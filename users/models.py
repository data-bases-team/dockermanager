from django.db import models
from django.contrib.auth.models import User
from unicodedata import name
from datetime import datetime, timedelta
from django.conf import settings


STATUS_CHOICES = [
    ('e', 'Enabled'),
    ('d', 'Disabled'),
]

class container(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    expdate = models.DateTimeField(default=(datetime.now() + timedelta(minutes = 10)))
    link = models.TextField(max_length=350, default=None, blank=True, null=True)
    port = models.IntegerField(unique=True, null=True, blank=True)
    userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    def __str__(self):
        return self.name
