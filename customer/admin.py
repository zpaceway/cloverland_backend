from django.contrib import admin
from customer.models import Customer
from django.contrib.auth.models import User, Group
from utils.common import make_link

admin.site.unregister(User)
admin.site.unregister(Group)


class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "email",
        "phone",
        "country",
        "state",
        "zip_code",
        "secret",
        "get_link",
    ]

    fields = [
        "id",
        "first_name",
        "last_name",
        "email",
        "phone",
        "country",
        "state",
        "zip_code",
        "secret",
        "get_link",
    ]

    readonly_fields = [
        "id",
        "secret",
        "get_link",
    ]

    @admin.display(description="Link")
    def get_link(self, obj: Customer):
        if not obj.id:
            return ""

        return make_link(
            url=obj.get_app_sign_in_link(), label=obj.get_app_sign_in_link()
        )


admin.site.register(Customer, CustomerAdmin)
