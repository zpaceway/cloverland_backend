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

    def representation(self, exclude_fields=None):
        exclude_fields = exclude_fields or set()
        return {
            "id": (self.id if not "id" in exclude_fields else ""),
            "name": (self.name if not "name" in exclude_fields else ""),
            "description": (
                self.description if not "description" in exclude_fields else ""
            ),
            "address": (self.address if not "address" in exclude_fields else ""),
            "price": (float(self.price) if not "price" in exclude_fields else 0),
            "symbol": NETWORK_SYMBOL,
            "endsAt": (
                self.ends_at.isoformat() if not "ends_at" in exclude_fields else ""
            ),
            "createdAt": (
                self.created_at.isoformat()
                if not "created_at" in exclude_fields
                else ""
            ),
            "updatedAt": (
                self.updated_at.isoformat()
                if not "updated_at" in exclude_fields
                else ""
            ),
            "walletAddressLink": self.get_wallet_address_link(),
        }

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "lotteries"
