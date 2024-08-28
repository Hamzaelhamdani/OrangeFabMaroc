# models.py

from django.db import models
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=200, default='Untitled Event')
    description = models.TextField(default='No description provided.')
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(default=timezone.now)
    place = models.CharField(max_length=200, default='TBD')
    form_link = models.URLField(default='https://example.com')
    banner_image = models.ImageField(upload_to='event_banners/', default='event_banners/default_banner.jpg')
    visible = models.BooleanField(default=True)  # New field for visibility status
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    