from django.http import JsonResponse
from rest_framework.views import APIView
from lottery.models import Lottery


class LotteryView(APIView):
    def get(self, request, lottery_id):
        lottery = Lottery.objects.get(id=lottery_id)
        response = JsonResponse(lottery.representation())

        return response


class LotteryListView(APIView):
    def get(self, request):
        lotteries = Lottery.objects.all().order_by("-created_at")
        response = JsonResponse(
            {"results": [lottery.representation() for lottery in lotteries]}
        )

        return response
