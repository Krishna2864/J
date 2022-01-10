from django.shortcuts import render

from django.db.models.query import QuerySet

from rest_framework.response import Response

from rest_framework import viewsets

from .models import *

from .serializers import *

class personal_info_viewset(viewsets.ModelViewSet):
    queryset = personal_info.objects.all()
    serializer_class= personal_info_serializer


class itr_type_viewset(viewsets.ModelViewSet):
    queryset = itr_type.objects.all()
    serializer_class= itr_type_serializer


class itrform_viewset(viewsets.ModelViewSet):
    queryset = itrform.objects.all()
    serializer_class= itrform_serializer


class exempted_income_viewset(viewsets.ModelViewSet):
    queryset = exempted_income.objects.all()
    serializer_class= exempted_income_serializer

class income_from_capital_viewset(viewsets.ModelViewSet):
    queryset = income_from_capital.objects.all()
    serializer_class= income_from_capital_serializer


class professional_income_viewset(viewsets.ModelViewSet):
    queryset = professional_income.objects.all()
    serializer_class= professional_income_serializer


class import_tds_viewset(viewsets.ModelViewSet):
    queryset = import_tds.objects.all()
    serializer_class= import_tds_serializer

######
y = 'tanviiii'



class Income_From_Salary_Pension_viewset(viewsets.ModelViewSet):
    queryset = Income_From_Salary_Pension.objects.all()
    serializer_class= Income_From_Salary_Pension_serializer




class Income_From_House_Property_viewset(viewsets.ModelViewSet):
    queryset = Income_From_House_Property.objects.all()
    serializer_class= Income_From_House_Property_serializer



class Income_from_Other_Sources_viewset(viewsets.ModelViewSet):
    queryset = Income_from_Other_Sources.objects.all()
    serializer_class= Income_from_Other_Sources_serializer


class Income_from_Business_Services_Profession_viewset(viewsets.ModelViewSet):
    queryset = Income_from_Business_Services_Profession.objects.all()
    serializer_class= Income_from_Business_Services_Profession_serializer


class Business_of_transport_viewset(viewsets.ModelViewSet):
    queryset = Business_of_transport.objects.all()
    serializer_class= Business_of_transport_serializer


class Other_Business_viewset(viewsets.ModelViewSet):
    queryset = Other_Business.objects.all()
    serializer_class= Other_Business_serializer

#####

class itr_products_viewset(viewsets.ModelViewSet):
    queryset = itr_products.objects.all()
    serializer_class= itr_products_serializer


