# board/urls.py
from django.urls import path
from .views import whiteboard

urlpatterns = [
    path('whiteboard/', whiteboard, name='whiteboard'),
]
