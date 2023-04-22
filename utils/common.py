from typing import Optional
from django.utils.safestring import mark_safe
import uuid


def prefixed_uuid_generator(prefix: str):
    def generate():
        return prefix + uuid.uuid4().hex[-12:]

    return generate


def make_link(
    url: str,
    label: str,
    taget: Optional[str] = "_blank",
):
    return mark_safe(f'<a href="{url}" target={taget}>{label}</a>')
