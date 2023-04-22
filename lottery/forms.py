from django import forms
from utils.blockchain import create_wallet
from utils.common import make_prefixed_uuid_generator


class LotteryForm(forms.ModelForm):
    id = forms.CharField(
        initial=make_prefixed_uuid_generator("LO"),
        widget=forms.widgets.TextInput(attrs={"readonly": True}),
    )

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
