from django.contrib import admin
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
        return make_link(url=obj.get_wallet_address_link(), label=obj.address)

    @admin.display(description="Lottery")
    def get_lottery(self, obj: Order):
        return make_link(url=obj.get_admin_link(), label=obj.lottery.__str__())

    @admin.display(description="Customer")
    def get_customer(self, obj: Order):
        return make_link(
            url=obj.customer.get_admin_link(), label=obj.customer.__str__()
        )

    @admin.display(description="Transaction")
    def get_transaction(self, obj: Order):
        if not obj.transaction_hash:
            return ""

        return make_link(url=obj.get_transaction_link(), label=obj.transaction_hash)

    @admin.display(description="Link")
    def get_link(self, obj: Order):

        return make_link(url=obj.get_app_link(), label=obj.get_app_link())


admin.site.register(Order, OrderAdmin)
