from .models import *
from rest_framework import serializers


class personal_info_serializer(serializers.ModelSerializer):
    class Meta:
        model = personal_info
        fields = ('__all__')


class itr_type_serializer(serializers.ModelSerializer):
    class Meta:
        model = itr_type
        fields = ('__all__')



class itrform_serializer(serializers.ModelSerializer):
    class Meta:
        model = itrform
        fields = ('__all__')



class exempted_income_serializer(serializers.ModelSerializer):
    class Meta:
        model = exempted_income
        fields = ('__all__')

class income_from_capital_serializer(serializers.ModelSerializer):
    class Meta:
        model = income_from_capital
        fields = ('__all__')

class professional_income_serializer(serializers.ModelSerializer):
    class Meta:
        model = professional_income
        fields = ('__all__')


class import_tds_serializer(serializers.ModelSerializer):
    class Meta:
        model = import_tds
        fields = ('__all__')



######
 #######
 
 
y = 'tanviiii'


class Income_From_Salary_Pension_serializer(serializers.ModelSerializer):
    class Meta:
        model = Income_From_Salary_Pension
        fields = ('__all__')


class Income_From_House_Property_serializer(serializers.ModelSerializer):
    class Meta:
        model = Income_From_House_Property
        fields = ('__all__')


class Income_from_Other_Sources_serializer(serializers.ModelSerializer):
    class Meta:
        model = Income_from_Other_Sources
        fields = ('__all__')


class Income_from_Business_Services_Profession_serializer(serializers.ModelSerializer):
    class Meta:
        model = Income_from_Business_Services_Profession
        fields = ('__all__')


class Business_of_transport_serializer(serializers.ModelSerializer):
    class Meta:
        model = Business_of_transport
        fields = ('__all__')


class Other_Business_serializer(serializers.ModelSerializer):
    class Meta:
        model = Other_Business
        fields = ('__all__')

#
class itr_products_serializer(serializers.ModelSerializer):
    class Meta:
        model = itr_products
        fields = ('__all__')

