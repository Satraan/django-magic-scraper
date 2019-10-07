from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MerchantSerializer
from .models import Merchant


class MerchantView(viewsets.ModelViewSet):
    serializer_class = MerchantSerializer
    queryset = Merchant.objects.all()
