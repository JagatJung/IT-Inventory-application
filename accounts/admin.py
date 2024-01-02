from django.contrib import admin
from .models import useraccounts , vendors, devices, devicetypes, issues
# Register your models here.

admin.site.register(useraccounts)

admin.site.register(vendors)

admin.site.register(devices)

admin.site.register(devicetypes)

admin.site.register(issues)
