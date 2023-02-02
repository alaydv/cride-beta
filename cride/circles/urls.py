"""URL's Circle"""

# Django
from django.urls import path

# Views
from .views import list_circles

app_name = 'circle'

urlpatterns = [
    path('circles/', list_circles),
]