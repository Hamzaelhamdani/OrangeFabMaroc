# content/views.py
from django.shortcuts import render, redirect
from .forms import LandingPageContentForm, PortfolioPageContentForm
from .models import LandingPageContent, PortfolioPageContent

def landing_page_view(request):
    content = LandingPageContent.objects.first()  # Assuming only one record for simplicity
    if request.method == 'POST':
        form = LandingPageContentForm(request.POST, instance=content)
        if form.is_valid():
            form.save()
            return redirect('content:landing_page')
    else:
        form = LandingPageContentForm(instance=content)
    return render(request, 'content/landing_page.html', {'form': form})

def portfolio_page_view(request):
    content = PortfolioPageContent.objects.first()  # Assuming only one record for simplicity
    if request.method == 'POST':
        form = PortfolioPageContentForm(request.POST, instance=content)
        if form.is_valid():
            form.save()
            return redirect('content:portfolio_page')
    else:
        form = PortfolioPageContentForm(instance=content)
    return render(request, 'content/portfolio_page.html', {'form': form})
