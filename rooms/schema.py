import graphene
from rooms.models import Room
from .types import RoomType, RoomListResponse


class Query(object):

    rooms = graphene.Field(RoomListResponse, page=graphene.Int())
    room = graphene.Field(RoomType, id=graphene.Int(required=True))

    def resolve_rooms(self, info, page=1):
        if page < 1:
            page = 1
        offset = 5
        start = offset * (page - 1)
        end = offset * page
        rooms = Room.objects.all()[start:end]
        total = Room.objects.count()
        return RoomListResponse(arr=rooms, total=total)

    def resolve_room(self, info, id):
        return Room.objects.get(id=id)
