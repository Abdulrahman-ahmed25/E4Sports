from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
#or
from rest_framework import generics

from .serializers import UserSerializer
from .models import SportNew

# @api_view(['GET'])
# def SportNew_list_api(request):
#     all_sportnew = SportNew.objects.all()
#     data = UserSerializer(all_sportnew, many=True).data
#     return Response({'data': data})

# @api_view(['GET'])
# def SportNew_detail_api(request, id):
#     news_detail = SportNew.objects.get(id=id)
#     data = UserSerializer(news_detail).data
#     return Response({'data': data})
class SportNewListApi(generics.ListCreateAPIView):
    queryset = SportNew.objects.all()
    serializer_class = UserSerializer

class SportNewDetailAPi(generics.RetrieveUpdateDestroyAPIView):
    queryset = SportNew.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'