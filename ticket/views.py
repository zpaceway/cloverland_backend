from django.http import JsonResponse
from rest_framework.views import APIView
from customer.models import Customer
from cloverland.env import APP_BASE_URL
from ticket.models import Ticket
from lottery.models import Lottery
from django.middleware.csrf import get_token
from utils.blockchain import create_wallet
from utils.common import make_prefixed_uuid_generator
from utils.communication import send_email
from django.db import transaction
from utils.http import submission


class TicketView(APIView):
    def get(self, request, ticket_id):
        ticket = Ticket.objects.get(id=ticket_id)
        ticket.validate()
        response = JsonResponse(ticket.representation())
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

        lottery_id = raw["lotteryId"]
        customer_info = raw["customerInfo"]
        lottery = Lottery.objects.get(id=lottery_id)

        first_name = customer_info.get("firstName")
        last_name = customer_info.get("lastName")
        email = customer_info.get("email")
        country = customer_info.get("country")
        phone = customer_info.get("phone")
        state = customer_info.get("state")
        zip_code = customer_info.get("zipCode")
        customer, new_customer = Customer.objects.get_or_create(
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

        ticket = Ticket.objects.create(
            id=make_prefixed_uuid_generator("OR")(),
            address=address,
            private_key=private_key,
            customer=customer,
            lottery=lottery,
        )

        ticket_app_url = f"{APP_BASE_URL}/ticket/{ticket.id}"

        send_email(
            to_emails=[email],
            subject="Ticket created",
            plain_text_content=(
                f"Your ticket #{ticket.id} was created, please follow the link down bellow to continue with your payment.\n\n"
                f"{ticket_app_url}\n\n"
                "Regards, Cloverland team."
            ),
        )

        return JsonResponse(
            {
                "ticket": ticket.representation(),
                "credentials": (
                    {
                        "id": customer.id,
                        "secret": customer.secret,
                    }
                    if new_customer
                    else {"id": "", "secret": ""}
                ),
            }
        )
