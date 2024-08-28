from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=200, default='Untitled News')
    description = models.TextField(default='No description provided.')
    date = models.DateField(default=timezone.now)
    place = models.CharField(max_length=200, default='TBD')
    tags = models.CharField(max_length=200, default='None')
    banner_image = models.ImageField(upload_to='news_banners/', default='news_banners/default_banner.jpg')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
