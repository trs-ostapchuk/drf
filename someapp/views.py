from django.shortcuts import render
from rest_framework import generics

from someapp.models import Women
from someapp.serializers import WomenSerializer


class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
