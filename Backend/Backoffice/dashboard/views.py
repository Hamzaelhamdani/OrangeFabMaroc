from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from startups.models import Startup  # Import du modèle Startup
from events.models import Event  # Import du modèle Event si nécessaire

@login_required
def index(request):
    # Récupérer le nombre total de startups
    startups_count = Startup.objects.count()
    
    # Récupérer d'autres informations (exemple : nombre d'événements)
    events_count = Event.objects.count()
    visitors_count = 12366  # Exemple de donnée statique
    subscribers_count = 35981  # Exemple de donnée statique
    db_startups_count = 69  # Exemple de donnée statique ou récupérée d'une source

    # Passer les données au template via le contexte
    context = {
        'startups_count': startups_count,
        'events_count': events_count,
        'visitors_count': visitors_count,
        'subscribers_count': subscribers_count,
        'db_startups_count': db_startups_count,
    }

    return render(request, 'dashboard/index.html', context)
