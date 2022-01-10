from .models import *
from rest_framework import serializers


class products_serializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = ('__all__')
