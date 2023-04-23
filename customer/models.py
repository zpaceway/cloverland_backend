from django.db import models

from cloverland.env import ADMIN_BASE_URL, APP_BASE_URL


class Customer(models.Model):
    id = models.CharField(
        max_length=36,
        primary_key=True,
    )
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128, unique=True)
    phone = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=128)
    secret = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_app_sign_in_link(self):
        return f"{APP_BASE_URL}/customer/?customerSecret={self.secret}&customerId={self.id}"

    def get_admin_link(self):
        return f"{ADMIN_BASE_URL}/admin/customer/customer/{self.id}/change/"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    def representation(self, exclude_fields=None):
        exclude_fields = exclude_fields or set()
        return {
            "id": (self.id if not "id" in exclude_fields else ""),
            "firstName": (
                self.first_name if not "first_name" in exclude_fields else ""
            ),
            "lastName": (self.last_name if not "last_name" in exclude_fields else ""),
            "fullName": (
                self.get_full_name() if not "full_name" in exclude_fields else ""
            ),
            "email": (self.email if not "email" in exclude_fields else ""),
            "phone": (self.phone if not "phone" in exclude_fields else ""),
            "country": (self.country if not "country" in exclude_fields else ""),
            "state": (self.state if not "state" in exclude_fields else ""),
            "zipCode": (self.zip_code if not "zip_code" in exclude_fields else ""),
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
            "orders": (
                ([order.representation(validate=False) for order in self.orders.all()])
                if not "orders" in exclude_fields
                else []
            ),
        }

    def __str__(self) -> str:
        return self.email
