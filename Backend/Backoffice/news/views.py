from datetime import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .models import News
from django.contrib import messages
from .forms import NewsForm
from django.http import JsonResponse
from datetime import datetime, timedelta

def news_view(request):
    today = datetime.today()
    start_of_week = today - timedelta(days=today.weekday())  # Start of the week (Monday)
    start_of_month = today.replace(day=1)  # Start of the current month

    news_this_week = News.objects.filter(date__range=[start_of_week, today])
    news_this_month = News.objects.filter(date__range=[start_of_month, today])
    all_news = News.objects.all()

    context = {
        'news_this_week': news_this_week,
        'news_this_month': news_this_month,
        'all_news': all_news,
    }
    return render(request, 'news.html', context)

def list_news(request):
    news_list = News.objects.all()
    return render(request, 'news/news_list.html', {'news_list': news_list})

def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    return JsonResponse({
        'title': news.title,
        'description': news.description,
        'date': news.date,
        'place': news.place,
        'tags': news.tags,
        'banner_image': news.banner_image.url
    })

def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "News added successfully")
            return redirect('news:list_news')
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})

def edit_news(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            messages.success(request, "News updated successfully")
            return redirect('news:list_news')
    else:
        form = NewsForm(instance=news)
    return render(request, 'news/edit_news.html', {'form': form})

def delete_news(request, news_id):
    news = get_object_or_404(News, id=news_id)
    news.delete()
    messages.success(request, "News deleted successfully")
    return redirect('news:list_news')
