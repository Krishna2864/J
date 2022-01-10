from django.shortcuts import render

from django.db.models.query import QuerySet

from rest_framework.response import Response

from rest_framework import viewsets

from .models import *

from .serializers import *

class tds_client_view(viewsets.ModelViewSet):
    queryset = tds_client.objects.all()
    serializer_class = tds_client_serializer

class search_tds_view(viewsets.ModelViewSet):
    queryset = search_tds.objects.all()
    serializer_class = search_tds_serializer

class search_tds_business_view(viewsets.ModelViewSet):
    queryset = search_tds_business.objects.all()
    serializer_class = search_tds_business_serializer

class order_enquiry_view(viewsets.ModelViewSet):
    queryset = order_enquiry.objects.all()
    serializer_class = order_enquiry_serializer

#####
class tds_or_tcs_products_view(viewsets.ModelViewSet):
    queryset = tds_or_tcs_products.objects.all()
    serializer_class = tds_or_tcs_products_serializer
