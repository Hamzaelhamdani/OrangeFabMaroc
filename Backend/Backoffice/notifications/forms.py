from django import forms
from .models import Proposition, RendezVous

class PropositionForm(forms.ModelForm):
    class Meta:
        model = Proposition
        fields = ['last_name', 'first_name', 'email', 'phone_number', 'startup_name', 'one_line_pitch', 'startup_link']


class RendezVousForm(forms.ModelForm):
    class Meta:
        model = RendezVous
        fields = ['last_name', 'first_name', 'email', 'phone_number', 'subject']
