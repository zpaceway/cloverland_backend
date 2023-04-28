from rest_framework import serializers

from customer.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(source="get_full_name")

    class Meta:
        model = Customer
        fields = [
            "id",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "phone",
            "country",
            "state",
            "zip_code",
            "created_at",
            "updated_at",
        ]

    def get_full_name(self, obj: Customer):
        return obj.get_full_name()
