from django.http import JsonResponse
from django.views import View
from cloverland.env import APP_BASE_URL
from utils.communication import send_email
from customer.models import Customer
from utils.http import submission


class CustomerView(View):
    def get(
        self,
        request,
        customer_id,
        customer_secret,
    ):
        customer = Customer.objects.get(
            id=customer_id,
            secret=customer_secret,
        )
        response = JsonResponse(customer.representation())

        return response


class CustomerAuthView(View):
    def post(self, request):
        raw = submission(request)
        customer = Customer.objects.get(email=raw["email"])
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
