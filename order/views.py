from django.http import JsonResponse
from django.views import View
from customer.models import Customer
from cloverland.env import APP_BASE_URL
from order.models import Order
from lottery.models import Lottery
from django.middleware.csrf import get_token
from utils.blockchain import create_wallet
from utils.common import make_prefixed_uuid_generator
from utils.communication import send_email
from django.db import transaction
from utils.http import submission


class OrderView(View):
    def get(self, request):
        order_id = request.GET.get("orderId")
        order = Order.objects.get(id=order_id)
        response = JsonResponse(order.representation())
        csrftoken = get_token(request)
        response.set_cookie(
            "csrftoken",
            csrftoken,
            samesite="Lax",
        )

        return response

    @transaction.atomic
    def post(self, request):
        raw = submission(request)

        lottery_id = raw.get("lotteryId")
        lottery = Lottery.objects.get(id=lottery_id)

        first_name = raw.get("firstName")
        last_name = raw.get("lastName")
        email = raw.get("email")
        country = raw.get("country")
        phone = raw.get("phone")
        state = raw.get("state")
        zip_code = raw.get("zipCode")
        customer, _ = Customer.objects.get_or_create(
            email=email,
            defaults={
                "id": make_prefixed_uuid_generator("CU")(),
                "first_name": first_name,
                "last_name": last_name,
                "country": country,
                "phone": phone,
                "state": state,
                "zip_code": zip_code,
                "secret": make_prefixed_uuid_generator("SE")(),
            },
        )

        address, private_key = create_wallet()

        order = Order.objects.create(
            id=make_prefixed_uuid_generator("OR")(),
            address=address,
            private_key=private_key,
            customer=customer,
            lottery=lottery,
        )

        order_app_url = f"{APP_BASE_URL}/order/{order.id}"

        send_email(
            to_emails=[email],
            subject="Order created",
            plain_text_content=(
                f"Your order #{order.id} was created, please follow the link down bellow to continue with your payment.\n\n"
                f"{order_app_url}\n\n"
                "Regards, Cloverland team."
            ),
        )

        return JsonResponse(order.representation())
