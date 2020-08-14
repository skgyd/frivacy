from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=20)
    image = models.CharField(max_length=255, default="")
    
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
    content = models.CharField(max_length=255, default="")

class Notice(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True)
    owner = models.CharField(max_length=20)
    content = models.CharField(max_length=255, default="")
    title = models.CharField(max_length=255, default="")