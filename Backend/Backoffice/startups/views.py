from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Startup
from .forms import StartupForm
from rest_framework import generics
from .serializers import StartupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class StartupListView(APIView):
    def get(self, request):
        startups = Startup.objects.all()
        serializer = StartupSerializer(startups, many=True)
        return Response(serializer.data)

def startup_list(request):
    startups = Startup.objects.all()
    return render(request, 'startups/startup_list.html', {'startups': startups})

def batch_list(request):
    startups = Startup.objects.all()
    years = startups.values_list('batch', flat=True).distinct()    
    selected_year = request.GET.get('year')
    if selected_year:
        startups = startups.filter(batch=selected_year)
    context = {
        'startups': startups,
        'years': years,
        'selected_year': selected_year,
    }
    return render(request, 'startups/batch_list.html', context)

def add_startup(request):
    if request.method == 'POST':
        form = StartupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('startups:list')
    else:
        form = StartupForm()
    return render(request, 'startups/startup_form.html', {'form': form})

def edit_startup(request, id):
    startup = get_object_or_404(Startup, id=id)
    if request.method == 'POST':
        form = StartupForm(request.POST, request.FILES, instance=startup)
        if form.is_valid():
            form.save()
            return redirect('startups:list')
    else:
        form = StartupForm(instance=startup)
    return render(request, 'startups/startup_form.html', {'form': form})

def delete_startup(request, id):
    startup = get_object_or_404(Startup, id=id)
    if request.method == 'POST':
        startup.delete()
        return redirect('startups:list')
    return render(request, 'startups/startup_confirm_delete.html', {'startup': startup})
