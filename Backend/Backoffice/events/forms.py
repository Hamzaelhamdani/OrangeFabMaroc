from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_date', 'end_date', 'start_time', 'end_time', 'place', 'form_link', 'banner_image', 'visible']