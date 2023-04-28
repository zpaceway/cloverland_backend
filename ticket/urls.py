from django.urls import path
from ticket.views import TicketCreateView, TicketView

urlpatterns = [
    path("", TicketCreateView.as_view()),
    path("<str:pk>/", TicketView.as_view()),
]
