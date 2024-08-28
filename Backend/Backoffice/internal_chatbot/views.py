from django.shortcuts import render, get_object_or_404, redirect
from .models import ChatbotQA
from .forms import ChatbotQAForm

def chatbot_dashboard(request):
    questions = ChatbotQA.objects.filter(requires_user_input=False)
    return render(request, 'internal_chatbot/chatbot_dashboard.html', {'questions': questions})

def edit_question(request, pk):
    question = get_object_or_404(ChatbotQA, pk=pk)
    if request.method == 'POST':
        form = ChatbotQAForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('chatbot_dashboard')
    else:
        form = ChatbotQAForm(instance=question)
    return render(request, 'internal_chatbot/edit_question.html', {'form': form})
