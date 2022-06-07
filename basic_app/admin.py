from django.contrib import admin
from basic_app.models import User
from basic_app.models import CustProfileInfo
from basic_app.models import VendorProfileInfo
# Register your models here.
admin.site.register(User)
admin.site.register(CustProfileInfo)
admin.site.register(VendorProfileInfo)
