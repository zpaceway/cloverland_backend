from typing import Optional
from django.utils.safestring import mark_safe
import uuid


class PrefixedShortUuidGenerator:
    prefix: str

    def __init__(self, prefix):
        self.prefix = prefix

    def generate(self):
        return self.prefix + uuid.uuid4().hex[-12:]


def make_link(
    url: str,
    label: str,
    taget: Optional[str] = "_blank",
):
    return mark_safe(f'<a href="{url}" target={taget}>{label}</a>')
