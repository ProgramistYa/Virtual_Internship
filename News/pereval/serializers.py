"""
Сериализаторы позволяют преобразовывать сложные данные, такие как наборы запросов и экземпляры модели,
в собственные типы данных Python, которые затем могут быть легко преобразованы
в JSON, XML или другие типы контента.
"""
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


class AuthEmailPerevalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval
        depth = 1
        # depyh  указывающее глубину взаимосвязей, которые должны быть пройдены перед возвратом к плоскому представлению.
        fields = '__all__'
