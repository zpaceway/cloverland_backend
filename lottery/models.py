from django.db import models
from tinymce import models as tinymce_models
from cloverland.env import APP_BASE_URL, NETWORK_BLOCK_EXPLORER_BASE_URL, NETWORK_SYMBOL


class Lottery(models.Model):
    id = models.CharField(
        max_length=36,
        primary_key=True,
    )
    name = models.CharField(max_length=128, unique=True)
    description = tinymce_models.HTMLField()
    address = models.CharField(max_length=128)
    private_key = models.CharField(max_length=128)
    price = models.FloatField()
    ends_at = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_app_link(self):
        return f"{APP_BASE_URL}/lottery/{self.id}"

    def get_wallet_address_link(self):
        return f"{NETWORK_BLOCK_EXPLORER_BASE_URL}/address/{self.address}"

    def representation(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "address": self.address,
            "price": float(self.price),
            "symbol": NETWORK_SYMBOL,
            "endsAt": self.ends_at.isoformat(),
            "createdAt": self.created_at.isoformat(),
            "updatedAt": self.updated_at.isoformat(),
            "walletAddressLink": self.get_wallet_address_link(),
        }

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "lotteries"
