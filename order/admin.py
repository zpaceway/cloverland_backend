from typing import Optional
from django.contrib import admin
from cloverland.env import ADMIN_BASE_URL, APP_BASE_URL, NETWORK_BLOCK_EXPLORER_BASE_URL
from order.models import Order
from utils.common import make_link


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "get_address",
        "get_lottery",
        "get_customer",
        "paid",
        "get_transaction",
        "get_link",
    ]
    readonly_fields = ["get_link"]

    @admin.display(description="Address")
    def get_address(self, obj: Order):
        address_url = f"{NETWORK_BLOCK_EXPLORER_BASE_URL}/address/{obj.address}"

        return make_link(url=address_url, label=obj.address)

    @admin.display(description="Lottery")
    def get_lottery(self, obj: Order):
        order_app_url = (
            f"{ADMIN_BASE_URL}/admin/lottery/lottery/{obj.lottery.id}/change/"
        )

        return make_link(url=order_app_url, label=obj.lottery.__str__())

    @admin.display(description="Customer")
    def get_customer(self, obj: Order):
        order_app_url = (
            f"{ADMIN_BASE_URL}/admin/customer/customer/{obj.customer.id}/change/"
        )

        return make_link(url=order_app_url, label=obj.customer.__str__())

    @admin.display(description="Transaction")
    def get_transaction(self, obj: Order):
        if not obj.transaction_hash:
            return ""

        transaction_url = f"{NETWORK_BLOCK_EXPLORER_BASE_URL}/tx/{obj.transaction_hash}"

        return make_link(url=transaction_url, label=obj.transaction_hash)

    @admin.display(description="Link")
    def get_link(self, obj: Order):
        order_app_url = f"{APP_BASE_URL}/order/{obj.id}"

        return make_link(url=order_app_url, label=order_app_url)


admin.site.register(Order, OrderAdmin)
