from django.urls import path
from .views import (
    home, 
    room, 
    create_room,
    update_room, 
    delete_room,
    login_page,
    logout_page,
    register_page,
    delete_message,
    user_profile,
    update_user,
    topics_page,
    activity_page
)


urlpatterns = [
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
    path('logout/', logout_page, name="logout"),
    path('', home, name="home"),
    path('room/<str:pk>', room, name="room"),
    path('profile/<str:pk>/', user_profile, name="user_profile"),
    path('create-room/', create_room, name='create_room'),
    path('update-room/<str:pk>/', update_room, name='update_room'),
    path('delete-room/<str:pk>/', delete_room, name='delete_room'),
    path('delete-message/<str:pk>/', delete_message, name='delete_message'),
    path('update-user', update_user, name='update_user'),
    path('topics/', topics_page, name='topics'),
    path('activity/', activity_page, name='activity'),
]