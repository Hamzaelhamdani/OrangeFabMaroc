from django.core.management.base import BaseCommand
from internal_chatbot.models import ChatbotQA

class Command(BaseCommand):
    help = 'Load initial chatbot questions and answers'

    def handle(self, *args, **kwargs):
        questions_and_answers = [
            {"question": "À propos de Orange Fab Maroc", "answer": "Orange Fab Maroc est le programme Orange d’accélération..."},
            {"question": "Connaître nos startups", "answer": "Choisissez comment vous souhaitez connaître nos startups..."},
            # Add all other questions and answers here
        ]

        for qa in questions_and_answers:
            ChatbotQA.objects.create(question=qa['question'], answer=qa['answer'])
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded initial questions and answers'))
