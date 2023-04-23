from django.db import models
from cloverland.env import (
    ADMIN_BASE_URL,
    APP_BASE_URL,
    NETWORK_BLOCK_EXPLORER_BASE_URL,
    NETWORK_UNIT,
)
from utils.blockchain import transfer, web3
from utils.communication import send_email


class Order(models.Model):
    id = models.CharField(
        max_length=36,
        primary_key=True,
    )
    address = models.CharField(max_length=128)
    private_key = models.CharField(max_length=128)
    lottery = models.ForeignKey(
        "lottery.Lottery", on_delete=models.CASCADE, related_name="orders"
    )
    customer = models.ForeignKey(
        "customer.Customer", on_delete=models.CASCADE, related_name="orders"
    )
    paid = models.BooleanField(default=False)
    transaction_hash = models.CharField(
        max_length=128,
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_wallet_address_link(self):
        return f"{NETWORK_BLOCK_EXPLORER_BASE_URL}/address/{self.address}"

    def get_app_link(self):
        return f"{APP_BASE_URL}/order/{self.id}"

    def get_transaction_link(self):
        return f"{NETWORK_BLOCK_EXPLORER_BASE_URL}/tx/{self.transaction_hash}"

    def get_admin_link(self):
        return f"{ADMIN_BASE_URL}/admin/lottery/lottery/{self.lottery.id}/change/"

    def representation(self):
        return {
            "id": self.id,
            "address": self.address,
            "paid": self.paid or self.validate(),
            "lottery": self.lottery.representation(),
            "customer": self.customer.representation(),
            "createdAt": self.created_at.isoformat(),
            "updatedAt": self.updated_at.isoformat(),
        }

    def validate(self):
        order_balance = web3.eth.get_balance(self.address)
        paid = order_balance >= web3.to_wei(self.lottery.price, NETWORK_UNIT)
        if paid:
            self.transaction_hash = transfer(
                to_wallet=self.lottery.address,
                from_wallet=self.address,
                private_key=self.private_key,
                value_wei=order_balance,
            )
            send_email(
                to_emails=[self.customer.email],
                subject="Order completed",
                plain_text_content=(
                    f"You have successfully completed your order #{self.id}.\n\n"
                    "Regards, Cloverland team."
                ),
            )

        self.paid = paid
        self.save()

        return self.paid

    def __str__(self) -> str:
        return self.id
