import django_filters
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework import generics
from rest_framework import mixins

from .filters import PerevalFilter
from .serializers import *
from .models import *


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImagesSerializer


class PerevalList(ListAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer


@api_view(['POST'])
def submit_data(request):
    serializer = PerevalSerializer(data=request.image)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
