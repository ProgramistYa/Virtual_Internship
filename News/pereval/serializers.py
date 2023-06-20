from .models import *
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email', 'phone', 'first_name', 'last_name',
            'surname'
        ]


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = [
            'latitude', 'longtitude', 'height'
        ]


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'title', 'image'
        ]


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = [
            'winter', 'summer', 'autumn', 'spring'
        ]


class PerevalSerializer(WritableNestedModelSerializer):
    user = UserSerializer()
    coord = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer()

    class Meta:
        model = Pereval
        fields = [
            'pk', 'status', 'beauty_title', 'title', 'other_titles',
            'connect', 'user', 'coord', 'level', 'images'
        ]