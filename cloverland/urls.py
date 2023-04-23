from django.contrib import admin
from django.urls import path, include
from customer.views import CustomerAuthView, CustomerView
from lottery.views import LotteryListView, LotteryView
from order.views import OrderView

urlpatterns = [
    path("grappelli/", include("grappelli.urls")),
    path("admin/", admin.site.urls),
    path("api/auth/", CustomerAuthView.as_view()),
    path(
        "api/customer/<str:customer_id>/<str:customer_secret>/", CustomerView.as_view()
    ),
    path("api/lottery/", LotteryListView.as_view()),
    path("api/lottery/<str:lottery_id>/", LotteryView.as_view()),
    path("api/order/", OrderView.as_view()),
    path("api/order/<str:order_id>/", OrderView.as_view()),
    path("tinymce/", include("tinymce.urls")),
]
