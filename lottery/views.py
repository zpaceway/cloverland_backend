from django.http import JsonResponse
from django.views import View
from lottery.models import Lottery


class LotteryView(View):
    def get(self, request, lottery_id):
        lottery = Lottery.objects.get(id=lottery_id)
        response = JsonResponse(lottery.representation())

        return response


class LotteryListView(View):
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
