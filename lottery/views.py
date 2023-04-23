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
        exclude_fields = ("description",)
        lotteries = Lottery.objects.filter().defer(*exclude_fields)
        response = JsonResponse(
            {
                "results": [
                    lottery.representation(exclude_fields=exclude_fields)
                    for lottery in lotteries
                ]
            }
        )

        return response
