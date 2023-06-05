from rest_framework import serializers
from .models import Room, Booked

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'tayp', 'capacity']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booked
        fields = ['id', 'start_time', 'end_time', 'room']