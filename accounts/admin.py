from django.contrib import admin
from .models import useraccounts , vendors, devices
# Register your models here.

admin.site.register(useraccounts)

admin.site.register(vendors)

admin.site.register(devices)
