from rest_framework import serializers
from cloverland.env import NETWORK_SYMBOL

from ticket.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    wallet_address_link = serializers.CharField(source="get_wallet_address_link")
    lottery_name = serializers.SerializerMethodField(source="get_lottery_name")
    lottery_price = serializers.SerializerMethodField(source="get_lottery_price")
    lottery_symbol = serializers.CharField(default=NETWORK_SYMBOL)

    class Meta:
        model = Ticket
        fields = [
            "id",
            "address",
            "paid",
            "lottery_id",
            "lottery_price",
            "lottery_name",
            "lottery_symbol",
            "created_at",
            "updated_at",
            "wallet_address_link",
        ]

    def get_lottery_name(self, obj: Ticket):
        return obj.lottery.name

    def get_lottery_price(self, obj: Ticket):
        return obj.lottery.price
