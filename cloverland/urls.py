from django.contrib import admin
from django.urls import path, include
from lottery.views import LotteryRecordsView, LotteryView
from ticket.views import TicketView

urlpatterns = [
    path("grappelli/", include("grappelli.urls")),
    path("admin/", admin.site.urls),
    path("api/customer/", include("customer.urls")),
    path("api/lottery/", include("lottery.urls")),
    path("api/ticket/", include("ticket.urls")),
    path("tinymce/", include("tinymce.urls")),
]
