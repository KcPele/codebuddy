from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import (
    UserSerializer,
    TopicSerializer,
    RoomSerializer

)
from base.models import (
    User,
    Topic, 
    Room,
    Message,
)
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/',
        'GET /api/users',
        'GET, CREATE /api/topics',
        'CRUD /api/rooms',
        
    ]
    return Response(routes)



## users
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


##topics
class TopicList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


##rooms
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)