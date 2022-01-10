from .models import *
from rest_framework import serializers

class tds_client_serializer(serializers.ModelSerializer):
    class Meta:
        model = tds_client
        fields = ('__all__')


class search_tds_serializer(serializers.ModelSerializer):
    class Meta:
        model = search_tds
        fields = ('__all__')

class search_tds_business_serializer(serializers.ModelSerializer):
    class Meta:
        model = search_tds_business
        fields = ('__all__')


class order_enquiry_serializer(serializers.ModelSerializer):
    class Meta:
        model = order_enquiry
        fields = ('__all__')

###

class tds_or_tcs_products_serializer(serializers.ModelSerializer):
    class Meta:
        model = tds_or_tcs_products
        fields = ('__all__')

