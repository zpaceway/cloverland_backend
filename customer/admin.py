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
    ]
    readonly_fields = [
        "id",
        "secret",
    ]


admin.site.register(Customer, CustomerAdmin)
