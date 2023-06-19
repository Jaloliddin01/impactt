from datetime import datetime, date

from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view

from .models import Room, Booked
from .serializers import RoomSerializer, BookSerializer

@api_view()
def get_rooms(request: Request) -> Response:

    res = {
        'page' : 1,
        'count': 0,
        'page_size' : 'infinity',
        'results' : []
    }

    try:
        rooms = Room.objects.all()
        res['count'] = rooms.count()
        serizalizer = RoomSerializer(rooms, many=True)
        res['results'] = list(dict(d) for d in serizalizer.data)
    except:
        pass

    return Response(res)

@api_view()
def detail_room(request: Request, pk: int) -> Response:
    try:
        room = Room.objects.get(pk=pk)
        serializer = RoomSerializer(room)
        return Response(serializer.data)
    except:
        res = {
            'error': "topilmadi"
        }
        return Response(res, status=status.HTTP_404_NOT_FOUND)


@api_view()
def availability(request: Request, pk: int) -> Response:
    try:
        if 'date' in request.query_params:
            today = request.query_params['date']
        else:
            today = (date.today().strftime('%Y-%m-%d'))
        print(today)
        room = Room.objects.get(pk=pk)
        booked_times = Booked.objects.filter(room=room, start_time__contains=today)
        serializer = BookSerializer(booked_times, many=True)
        for i in range(len(serializer.data)):
            print(date_formater(serializer.data[i]['start_time']))
            print(date_formater(serializer.data[i]['end_time']))

        return Response(serializer.data)
    except Booked.DoesNotExist:
        res = {
            "error": "Bunday xona topilmadi"
        }
        return Response(res)


@api_view(['GET', 'POST'])
def book(request: Request) -> Response:
    pass


def date_formater(date: str):
    if 'T' in date:
        d = date.split('T')
        dt = d[0]
        ds = dt.split('-')
        dt = ds[2] + "-" + ds[1] + "-" + ds[0]
        dt += " " + d[1].split('Z')[0]
    else:
        ds = date.split('-')
        dt = ds[2] + "-" + ds[1] + "-" + ds[0]
    return dt

