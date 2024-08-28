# content/models.py
from django.db import models

class LandingPageContent(models.Model):
    header = models.CharField(max_length=255)
    welcome_text = models.TextField()
    section_text = models.TextField()
    footer_text = models.TextField()

class PortfolioPageContent(models.Model):
    header = models.CharField(max_length=255)
    welcome_text = models.TextField()
    section_text = models.TextField()
    footer_text = models.TextField()
    startup_batches = models.TextField()  # Text field to store comma-separated batch info
