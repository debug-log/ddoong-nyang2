from myapp.models import *
from myapp.serializers import *
from rest_framework import generics

class DietInfoList(generics.ListCreateAPIView):
    queryset = DietInfo.objects.all()
    serializer_class = DietInfoSerializer

class DietInfoDetail(generics.RetrieveDestroyAPIView):
    queryset = DietInfo.objects.all()
    serializer_class = DietInfoSerializer