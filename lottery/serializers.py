from rest_framework import serializers
from cloverland.env import NETWORK_SYMBOL

from lottery.models import Lottery


class LotterySerializer(serializers.ModelSerializer):
    symbol = serializers.ReadOnlyField(default=NETWORK_SYMBOL)
    wallet_address_link = serializers.CharField(source="get_wallet_address_link")

    class Meta:
        model = Lottery
        fields = [
            "id",
            "name",
            "description",
            "address",
            "price",
            "symbol",
            "ends_at",
            "created_at",
            "updated_at",
            "wallet_address_link",
        ]

    def get_wallet_address_link(self, obj: Lottery):
        return obj.get_wallet_address_link()
