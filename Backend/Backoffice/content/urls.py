# content/urls.py
from django.urls import path
from .views import landing_page_view, portfolio_page_view

app_name = 'content'

urlpatterns = [
    path('', landing_page_view, name='landing_page'),
    path('portfolio/', portfolio_page_view, name='portfolio_page'),
]
