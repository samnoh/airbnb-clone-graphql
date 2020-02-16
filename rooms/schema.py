import graphene
from graphene_django import DjangoObjectType
from rooms.models import Room


class RoomType(DjangoObjectType):
    class Meta:
        model = Room


class RoomListResponse(graphene.ObjectType):

    arr = graphene.List(RoomType)
    total = graphene.Int()


class Query(object):

    rooms = graphene.Field(RoomListResponse, page=graphene.Int())

    def resolve_rooms(self, info, page=1):
        offset = 5
        start = offset * (page - 1)
        end = offset * page
        rooms = Room.objects.all()[start:end]
        total = Room.objects.count()
        return RoomListResponse(arr=rooms, total=total)
