from django.db import models

# Create your models here.
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# DB ORM
class Image(models.Model):
    image = ProcessedImageField(
        processors=[ResizeToFill(500, 500)],
        format='JPEG',
        options={'quality': 90},
    )