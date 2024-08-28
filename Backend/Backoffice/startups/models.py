from django.db import models

class Startup(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
    logo = models.ImageField(upload_to='startup_logos/')
    year = models.IntegerField()
    tags = models.CharField(max_length=200)
    batch = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True) 
    
    def __str__(self):
        return self.name
