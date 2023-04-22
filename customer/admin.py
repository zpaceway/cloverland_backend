from django.contrib import admin
from customer.models import Customer
from django.contrib.auth.models import User, Group

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
    readonly_fields = [
        "id",
        "secret",
    ]

    @admin.display(description="Link")
    def get_link(self, obj: Customer):
        if not obj.id:
            return ""

        order_app_url = f"{APP_BASE_URL}/lottery/{obj.id}"

        return make_link(url=order_app_url, label=order_app_url)


admin.site.register(Customer, CustomerAdmin)
