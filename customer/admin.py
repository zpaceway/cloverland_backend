from django.contrib import admin
from customer.models import Customer
from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Customer)
