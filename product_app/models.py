from django.db import models
import uuid

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(
        max_length=500)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    logo = models.ImageField(upload_to='logos', blank=True, null=True)
    rotate_duration = models.FloatField(
        null=True, blank=True
        )