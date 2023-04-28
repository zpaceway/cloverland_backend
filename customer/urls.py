from django.urls import path
from customer.views import CustomerAuthView, CustomerView

urlpatterns = [
    path("auth/", CustomerAuthView.as_view()),
    path("<str:pk>/<str:secret>/", CustomerView.as_view()),
]
