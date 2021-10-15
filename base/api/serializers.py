from base.models import User, Room, Topic, Message
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    rooms = serializers.PrimaryKeyRelatedField(many=True, queryset=Room.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'rooms']


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'