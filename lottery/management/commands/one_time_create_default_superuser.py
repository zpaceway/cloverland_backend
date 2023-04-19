from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import os

DEFAULT_SUPERUSER_USERNAME = os.getenv("DEFAULT_SUPERUSER_USERNAME")
DEFAULT_SUPERUSER_FIRST_NAME = os.getenv("DEFAULT_SUPERUSER_FIRST_NAME")
DEFAULT_SUPERUSER_LAST_NAME = os.getenv("DEFAULT_SUPERUSER_LAST_NAME")
DEFAULT_SUPERUSER_EMAIL = os.getenv("DEFAULT_SUPERUSER_EMAIL")
DEFAULT_SUPERUSER_PASSWORD = os.getenv("DEFAULT_SUPERUSER_PASSWORD")


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.get_or_create(
            username=DEFAULT_SUPERUSER_USERNAME,
            defaults={
                "is_staff": True,
                "is_superuser": True,
                "first_name": DEFAULT_SUPERUSER_FIRST_NAME,
                "last_name": DEFAULT_SUPERUSER_LAST_NAME,
                "email": DEFAULT_SUPERUSER_EMAIL,
                "password": make_password(DEFAULT_SUPERUSER_PASSWORD),
            },
        )
