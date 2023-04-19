from django.contrib import admin
from django.urls import path, include
from lottery.views import LotteryView
from order.views import OrderView

urlpatterns = [
    path("grappelli/", include("grappelli.urls")),  # grappelli URLS
    path("admin/", admin.site.urls),
    path("api/order", OrderView.as_view()),
    path("api/lottery", LotteryView.as_view()),
    path("tinymce/", include("tinymce.urls")),
]
