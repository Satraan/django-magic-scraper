from rest_framework import serializers
from .models import Merchant, Card


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = ('id', 'title', 'website')


class CardSerializer(serializers.ModelSerializer):
    # Data fields
    scryfallId = models.UUIDField(editable=True, null=True)
    oracleId = models.UUIDField(blank=True)
    uri = models.CharField(blank=True, max_length=1000)
    scryfallUri = models.CharField(blank=True, max_length=1000)

    # Card info fields
    name = models.CharField(max_length=1000)
    cmc = models.IntegerField(blank=True)
    typeLine = models.CharField(blank=True, max_length=1000)
    oracleText = models.CharField(blank=True, max_length=1000, null=True)
    manaCost = models.CharField(blank=True, max_length=1000)
    colors = models.TextField(blank=True)
    colorIdentity = models.TextField(blank=True, null=True)

    # Print / collector fields
    collectorNumber = models.CharField(blank=True, max_length=1000)
    imageLinks = models.TextField(blank=True, null=True)
    smallImage = models.TextField(blank=True, null=True)
    rarity = models.CharField(blank=True, max_length=1000)
    tcgPrice = models.DecimalField(
        blank=True, null=True, max_digits=5, decimal_places=2, default=0.00)
