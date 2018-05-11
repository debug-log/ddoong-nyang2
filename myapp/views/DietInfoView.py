from myapp.models import *
from myapp.serializers import *
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt

class DietInfoList(generics.ListCreateAPIView):
	@csrf_exempt
    queryset = DietInfo.objects.all()
    serializer_class = DietInfoSerializer

class DietInfoDetail(generics.RetrieveDestroyAPIView):
	@csrf_exempt
    queryset = DietInfo.objects.all()
    serializer_class = DietInfoSerializer