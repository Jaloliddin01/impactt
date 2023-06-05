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
def availability(request: Request) -> Response:
    pass

@api_view(['GET', 'POST'])
def book(request: Request) -> Response:
    pass

