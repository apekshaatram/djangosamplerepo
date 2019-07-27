from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from djangosample.initialapp.models import *
from djangosample.initialapp.serializer import *

class ProductVset(ModelViewSet):
    queryset=product.objects.all()
    serializer_class=ProductSer

class VendorVset(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSer

