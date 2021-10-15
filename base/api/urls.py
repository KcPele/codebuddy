from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    getRoutes,
    UserViewSet,
    TopicList,
    RoomViewSet,

)


router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'users', UserViewSet)
urlpatterns = [
    path('', getRoutes),
    path('topics/', TopicList.as_view()),
    path('', include(router.urls))
   
]