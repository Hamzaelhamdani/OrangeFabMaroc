from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', views.notification_list, name='notification_list'),
    path('create_proposition/', views.create_proposition, name='create_proposition'),
    path('create_rendezvous/', views.create_rendezvous, name='create_rendezvous'),
]
