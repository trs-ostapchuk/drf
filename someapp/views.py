from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from someapp.models import Women
from someapp.serializers import WomenSerializer


class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# use Basic view class APIView
class WomenAPI(APIView):
    def get(self, request):
        lst = Women.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        new_post = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        # function 'model_to_dict()' recreate 'new_post' to dictionary
        return Response({'post': model_to_dict(new_post)})
# end use Basic view class APIView
