from django.http import JsonResponse
from rest_framework import generics
from lottery.models import Lottery
from lottery.serializers import LotterySerializer


class LotteryView(generics.RetrieveAPIView):
    queryset = Lottery.objects.all()
    serializer_class = LotterySerializer


class LotteryRecordsView(generics.ListAPIView):
    queryset = Lottery.objects.all()
    serializer_class = LotterySerializer
