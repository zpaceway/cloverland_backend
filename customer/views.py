from django.http import JsonResponse
from rest_framework import generics
from cloverland.env import APP_BASE_URL
from cloverland.mixins import MultipleFieldsLookupMixin
from customer.serializers import CustomerSerializer
from utils.communication import send_email
from customer.models import Customer


class CustomerView(generics.RetrieveAPIView, MultipleFieldsLookupMixin):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_fields = ["pk", "secret"]


class CustomerAuthView(generics.GenericAPIView):
    def post(self, request):
        customer = Customer.objects.get(email=request.data["email"])
        customer_app_url = f"{APP_BASE_URL}/customer/?customerSecret={customer.secret}&customerId={customer.id}"

        send_email(
            to_emails=[customer.email],
            subject="Login to Cloverland",
            plain_text_content=(
                f"Hi {customer.first_name} {customer.last_name}, you requested a magic link to login "
                f"to cloverland. Follow this link {customer_app_url} to login.\n\n"
                "Regards, Cloverland Team."
            ),
        )
        return JsonResponse({"status": "success"})
