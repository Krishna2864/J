from .models import *
from rest_framework import serializers


### serializers =>

class apply_for_GST_Registration_serializer(serializers.ModelSerializer):
    class Meta:
        model = apply_for_GST_Registration
        fields = ('__all__')

class GST_Status_serializer(serializers.ModelSerializer):
    class Meta:
        model = GST_Status
        fields = ('__all__')


class GST_Return_Client_Details_serializer(serializers.ModelSerializer):
    class Meta:
        model = GST_Return_Client_Details
        fields = ('__all__')


class GST_Return_Select_GST_Type_serializer(serializers.ModelSerializer):
    class Meta:
        model = GST_Return_Select_GST_Type
        fields = ('__all__')

class view_all_review_gst_form_serializer(serializers.ModelSerializer):
    class Meta:
        model = view_all_review_gst_form
        fields = ('__all__')


###

class gst_products_serializer(serializers.ModelSerializer):
    class Meta:
        model = gst_products
        fields = ('__all__')
