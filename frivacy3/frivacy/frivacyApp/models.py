from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.

class User(models.Model):
    is_authenticated = True
    userid = models.CharField(max_length=200, default="")
    name = models.CharField(max_length=20, default="")
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    sign_up_date = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    profilepic = models.CharField(max_length=255, default="")
    class Meta: #메타 클래스를 이용하여 테이블명 지정
        db_table = 'test_user'

class Image(models.Model):
    image = ProcessedImageField(
        processors=[ResizeToFill(400, 400)],
        format='JPEG',
        options={'quality': 90},
    )

class Post(models.Model):
    image = models.CharField(max_length=255)
    date_uploaded = models.DateTimeField(auto_now=True)
    owner = models.CharField(max_length=20)
    content = models.CharField(max_length=140, default="")