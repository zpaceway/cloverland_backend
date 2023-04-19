from django.http import JsonResponse
from django.views import View
from lottery.models import Lottery


class LotteryView(View):
    def get(self, request):
        lottery_id = request.GET.get("lotteryId")
        lottery = Lottery.objects.get(id=lottery_id)
        response = JsonResponse(lottery.representation())

        return response
