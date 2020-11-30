from django.db import models
import uuid
import time
from PIL import Image as Img
from io import BytesIO
from django.core.files.base import ContentFile

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(
        max_length=500)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    logo = models.ImageField(upload_to='logos', blank=True, null=True)
    rotate_duration = models.FloatField(editable=False)
    modified = models.BooleanField(default=False, editable=False)

    def save(self, *args, **kwargs):
        if self.logo:
            image = Img.open(self.logo)
            start_time = time.time()
            image = image.rotate(180)
            self.rotate_duration = time.time() - start_time
            image_io = BytesIO()
            image.save(image_io, format='jpeg', quality=100)
            self.logo = ContentFile(image_io.getvalue(), 'logo.jpg')
        else:
            self.rotate_duration = 0
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-updated']