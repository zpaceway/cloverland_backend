from django.contrib import admin
from cloverland.env import NETWORK_SYMBOL
from lottery.forms import LotteryForm
from lottery.models import Lottery
from utils.common import make_link


class LotteryAdmin(admin.ModelAdmin):
    form = LotteryForm
    list_display = [
        "id",
        "name",
        "get_price",
        "get_address",
        "created_at",
        "updated_at",
        "ends_at",
        "get_link",
    ]

    fields = (
        [
            "id",
            "address",
            "private_key",
        ]
        + LotteryForm.Meta.fields
        + ["get_link"]
    )

    readonly_fields = [
        "address",
        "private_key",
        "get_link",
    ]

    @admin.display(description="Price")
    def get_price(self, obj: Lottery):
        return f"{float(obj.price)} {NETWORK_SYMBOL}"

    @admin.display(description="Link")
    def get_link(self, obj: Lottery):
        if not obj.id:
            return ""

        return make_link(url=obj.get_app_link(), label=obj.get_app_link())

    @admin.display(description="Address")
    def get_address(self, obj: Lottery):
        return make_link(url=obj.get_wallet_address_link(), label=obj.address)


admin.site.register(Lottery, LotteryAdmin)
