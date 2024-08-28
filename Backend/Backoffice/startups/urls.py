from django.urls import path
from . import views
from .views import StartupListView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'startups'

urlpatterns = [
    path('', views.startup_list, name='list'),
    path('add/', views.add_startup, name='add'),
    path('<int:id>/edit/', views.edit_startup, name='edit'),
    path('<int:id>/delete/', views.delete_startup, name='delete'),
    path('api/startups/', StartupListView.as_view(), name='startup-list'),
    path('batch/', views.batch_list, name='batch_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)