from django.shortcuts import render, redirect
from .models import Proposition, RendezVous
from .forms import PropositionForm, RendezVousForm

def notification_list(request):
    propositions = Proposition.objects.all().order_by('-created_at')
    rendezvous = RendezVous.objects.all().order_by('-created_at')
    return render(request, 'notifications/notification_list.html', {
        'propositions': propositions,
        'rendezvous': rendezvous,
    })


def create_proposition(request):
    if request.method == 'POST':
        form = PropositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notifications:notification_list')
    else:
        form = PropositionForm()
    return render(request, 'notifications/create_proposition.html', {'form': form})


def create_rendezvous(request):
    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notifications:notification_list')
    else:
        form = RendezVousForm()
    return render(request, 'notifications/create_rendezvous.html', {'form': form})
