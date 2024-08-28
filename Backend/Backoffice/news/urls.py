from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.list_news, name='list_news'),
    path('add/', views.add_news, name='add_news'),
    path('edit/<int:news_id>/', views.edit_news, name='edit_news'),
    path('delete/<int:news_id>/', views.delete_news, name='delete_news'),
]
