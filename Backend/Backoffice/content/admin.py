# content/admin.py
from django.contrib import admin
from .models import LandingPageContent, PortfolioPageContent

admin.site.register(LandingPageContent)
admin.site.register(PortfolioPageContent)
