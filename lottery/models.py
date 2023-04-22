from django.db import models
from tinymce import models as tinymce_models
import os

NETWORK_SYMBOL = os.getenv("NETWORK_SYMBOL")


class Lottery(models.Model):
    id = models.CharField(
        max_length=36,
        primary_key=True,
    )
    name = models.CharField(max_length=128, unique=True)
    description = tinymce_models.HTMLField()
    address = models.CharField(max_length=128)
    private_key = models.CharField(max_length=128)
    price = models.DecimalField(decimal_places=18, max_digits=36)
    ends_at = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
        }

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "lotteries"
