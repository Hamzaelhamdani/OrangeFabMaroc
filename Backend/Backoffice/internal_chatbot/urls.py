from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.chatbot_dashboard, name='chatbot_dashboard'),
    path('edit/<int:pk>/', views.edit_question, name='edit_question'),
]
