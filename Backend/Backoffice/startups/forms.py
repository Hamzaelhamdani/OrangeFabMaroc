from django import forms
from .models import Startup

class StartupForm(forms.ModelForm):
    class Meta:
        model = Startup
        fields = ['name', 'description', 'link', 'logo', 'year', 'tags', 'batch', 'city']
