from django import forms
import uuid
from utils.blockchain import create_wallet


class LotteryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        fields = [
            "name",
            "description",
            "price",
            "ends_at",
        ]

    def save(self, commit=True):
        if not self.instance.address or not self.instance.private_key:
            address, private_key = create_wallet()
            self.instance.address = address
            self.instance.private_key = private_key
        return super().save(commit)
