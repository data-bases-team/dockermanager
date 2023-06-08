from django.db import models
from django.contrib.auth.models import User
from unicodedata import name
from datetime import datetime, timedelta
from django.conf import settings
from crum import get_current_user


STATUS_CHOICES = [
    ('e', 'Enabled'),
    ('d', 'Disabled'),
]

class container(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,unique=True)
    login = models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='e')
    expdate = models.DateTimeField(default=(datetime.now() + timedelta(minutes = 10)))
    link = models.TextField(max_length=350, default=None, blank=True, null=True)
    port = models.IntegerField(unique=True, null=True, blank=True)
    userid = models.ForeignKey('auth.User', on_delete=models.CASCADE,  blank=True, null=True, default=None)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.userid = user
        #self.modified_by = user
        super(container, self).save(*args, **kwargs)
