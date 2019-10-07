from django.contrib import admin

# Register your models here.
from .models import Merchant


class MerchantAdmin(admin.ModelAdmin):
    list_display = ('title', 'website')


# Register your models here.
admin.site.register(Merchant, MerchantAdmin)
