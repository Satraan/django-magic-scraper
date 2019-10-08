from django.contrib import admin

# Register your models here.
from .models import Merchant, Card


class MerchantAdmin(admin.ModelAdmin):
    list_display = ('title', 'website')


class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'rarity', 'oracleText', 'scryfallId')


# Register your models here.
admin.site.register(Merchant, MerchantAdmin)
admin.site.register(Card, CardAdmin)
