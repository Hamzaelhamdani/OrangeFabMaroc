# events/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Event
from .forms import EventForm
from .serializers import EventSerializer

class EventListView(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

def event_list(request):
    events = Event.objects.all().order_by('start_date')
    return render(request, 'events/event_list.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('events:event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

def edit_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events:event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form})

def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        event.delete()
        return redirect('events:event_list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})

def toggle_visibility(request, id):
    event = get_object_or_404(Event, id=id)
    event.visible = not event.visible
    event.save()
    return JsonResponse({'status': 'success', 'visible': event.visible})
