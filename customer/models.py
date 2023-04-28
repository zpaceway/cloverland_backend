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

    def __str__(self) -> str:
        return self.email
