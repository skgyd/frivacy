from __future__ import unicode_literals
from django.db import models
from six import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class User(models.Model):
    is_authenticated = True
    userid = models.CharField(max_length=200, default="")
    name = models.CharField(max_length=20, default="")
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    sign_up_date = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    profilepic = models.CharField(max_length=255, default="")
