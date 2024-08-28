from django import forms
from .models import ChatbotQA

class ChatbotQAForm(forms.ModelForm):
    class Meta:
        model = ChatbotQA
        fields = ['question', 'answer']
