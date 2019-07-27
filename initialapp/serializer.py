from rest_framework.serializers import ModelSerializer
from djangosample.initialapp.models import *

class ProductSer(ModelSerializer):
    class Meta:
        model=product
        fields='__all__'

class VendorSer(ModelSerializer):
    class Meta:
        model=Vendor
        fields='__all__'
