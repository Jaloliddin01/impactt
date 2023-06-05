from django.urls import path

urlpatterns = [
    path('rooms/'),
    path('rooms/<int:pk>/'),
    path('rooms/<int:pk>/availability/'),
    path('rooms/<int:pk>/book/'),
]   