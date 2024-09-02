from django.shortcuts import render
from rest_framework import viewsets
from .models import Novel
from .serializers import NovelSerializer

# Create your views here.


class NovelViewset(viewsets.ModelViewSet):
    queryset = Novel.objects.all()
    serializer_class = NovelSerializer
