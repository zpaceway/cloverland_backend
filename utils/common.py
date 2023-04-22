from typing import Optional
from django.utils.safestring import mark_safe
import uuid
import random


def make_prefixed_uuid_generator(prefix: str):
    def generate():
        unique_part = uuid.uuid4().hex[-12:]
        unique_part_randomized_uppercase = ""
        for c in unique_part:
            c = c if random.randint(0, 1) else c.upper()
            unique_part_randomized_uppercase += c
        return prefix + unique_part_randomized_uppercase

    return generate


def make_link(
    url: str,
    label: str,
    taget: Optional[str] = "_blank",
):
    return mark_safe(f'<a href="{url}" target={taget}>{label}</a>')
