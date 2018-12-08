# from django.shortcuts import render

from rest_framework import viewsets
from .models import Mumin
from .serializers import MuminSerializer
# Create your views here.


class MuminViewSet(viewsets.ModelViewSet):
    queryset = Mumin.objects.all()
    serializer_class = MuminSerializer
