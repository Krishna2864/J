from .models import *
from rest_framework import serializers







class roc_serializer(serializers.ModelSerializer):
    class Meta:
        model = roc
        fields = ('__all__')
