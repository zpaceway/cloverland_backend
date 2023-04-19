from typing import Optional
from django.utils.safestring import mark_safe
import shortuuid


class PrefixedShortUuidGenerator:
    prefix: str

    def __init__(self, prefix):
        self.prefix = prefix

    def generate(self):
        return self.prefix + shortuuid.uuid()


def make_link(
    url: str,
    label: str,
    taget: Optional[str] = "_blank",
):
    return mark_safe(f'<a href="{url}" target={taget}>{label}</a>')
