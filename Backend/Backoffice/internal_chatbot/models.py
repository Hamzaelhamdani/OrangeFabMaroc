from django.db import models

class ChatbotQA(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    requires_user_input = models.BooleanField(default=False)

    def __str__(self):
        return self.question
