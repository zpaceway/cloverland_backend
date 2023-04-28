from django.http import JsonResponse
from rest_framework import generics
from customer.models import Customer
from cloverland.env import APP_BASE_URL
from ticket.models import Ticket
from lottery.models import Lottery
from ticket.serializers import TicketSerializer
from utils.blockchain import create_wallet
from utils.common import make_prefixed_uuid_generator
from utils.communication import send_email
from django.db import transaction
from utils.http import submission


class TicketView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_object(self):
        obj = super().get_object()
        obj.validate()
        return obj


class TicketCreateView(generics.GenericAPIView):
    @transaction.atomic
    def post(self, request):
        raw = submission(request)

        lottery_id = raw["lottery_id"]
        customer_info = raw["customer_info"]
        lottery = Lottery.objects.get(id=lottery_id)

        first_name = customer_info.get("first_name")
        last_name = customer_info.get("last_name")
        email = customer_info.get("email")
        country = customer_info.get("country")
        phone = customer_info.get("phone")
        state = customer_info.get("state")
        zip_code = customer_info.get("zip_code")
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
            id=make_prefixed_uuid_generator("TK")(),
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
                "ticket": TicketSerializer(instance=ticket).data,
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
