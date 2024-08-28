# content/forms.py
from django import forms
from .models import LandingPageContent, PortfolioPageContent

class LandingPageContentForm(forms.ModelForm):
    class Meta:
        model = LandingPageContent
        fields = ['header', 'welcome_text', 'section_text', 'footer_text']

class PortfolioPageContentForm(forms.ModelForm):
    class Meta:
        model = PortfolioPageContent
        fields = ['header', 'welcome_text', 'section_text', 'footer_text', 'startup_batches']
