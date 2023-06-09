from django.urls import path
from .views import get_rooms, detail_room, availability, book

urlpatterns = [
    path('rooms/', get_rooms),
    path('rooms/<int:pk>/', detail_room),
    path('rooms/<int:pk>/availability/', availability),
    path('rooms/<int:pk>/book/', book),
]   