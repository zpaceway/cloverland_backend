from django.urls import path
from lottery.views import LotteryRecordsView, LotteryView

urlpatterns = [
    path("", LotteryRecordsView.as_view()),
    path("<str:pk>/", LotteryView.as_view()),
]
