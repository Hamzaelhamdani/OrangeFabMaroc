from django.urls import path, include
from . import views
from .views import EventViewSet
from rest_framework.routers import DefaultRouter
from .views import EventListView

app_name = 'events'

router = DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('add/', views.add_event, name='add_event'),
    path('edit/<int:id>/', views.edit_event, name='edit_event'),
    path('delete/<int:id>/', views.delete_event, name='delete_event'),
    path('toggle_visibility/<int:id>/', views.toggle_visibility, name='toggle_visibility'),
    path('api/events/', EventListView.as_view(), name='api_events'),
]
