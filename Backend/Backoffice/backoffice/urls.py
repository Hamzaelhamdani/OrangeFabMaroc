from django.contrib import admin
from django.urls import path, include
from dashboard import views as dashboard_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),
    path('', dashboard_views.index, name='home'),
    path('events/', include('events.urls')),
    path('news/', include('news.urls')),
    path('startups/', include('startups.urls', namespace='startups')),
    path('internal_chatbot/', include('internal_chatbot.urls')),
    path('notifications/', include('notifications.urls', namespace='notifications')),
    path('chatbot/', include('chatbot.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
