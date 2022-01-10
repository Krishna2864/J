
from rest_framework import viewsets

from .models import *

from .serializers import *


# gst views =>


class apply_for_GST_Registration_viewset(viewsets.ModelViewSet):
    queryset = apply_for_GST_Registration.objects.all()
    serializer_class= apply_for_GST_Registration_serializer


class GST_Status_viewset(viewsets.ModelViewSet):
    queryset = GST_Status.objects.all()
    serializer_class= GST_Status_serializer


class GST_Return_Client_Details_viewset(viewsets.ModelViewSet):
    queryset = GST_Return_Client_Details.objects.all()
    serializer_class= GST_Return_Client_Details_serializer


class GST_Return_Select_GST_Type_viewset(viewsets.ModelViewSet):
    queryset = GST_Return_Select_GST_Type.objects.all()
    serializer_class= GST_Return_Select_GST_Type_serializer


class view_all_review_gst_form_viewset(viewsets.ModelViewSet):
    queryset = view_all_review_gst_form.objects.all()
    serializer_class= view_all_review_gst_form_serializer


class gst_products_viewset(viewsets.ModelViewSet):
    queryset = gst_products.objects.all()
    serializer_class= gst_products_serializer