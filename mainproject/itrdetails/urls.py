from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views  import *
router = DefaultRouter()

router.register(r'personalinfo',personal_info_viewset,basename='personalinfo'),
router.register(r'itrtype',itr_type_viewset,basename='itrtype'),
router.register(r'itrform',itrform_viewset,basename='itrform'),
router.register(r'exempted_income',exempted_income_viewset,basename='exempted_income'),
router.register(r'income_from_capital',income_from_capital_viewset,basename='income_from_capital'),
router.register(r'professional_income',professional_income_viewset,basename='professional_income'),
router.register(r'import_tds',import_tds_viewset,basename='import_tds'),

######


router.register(r'Income_From_Salary_Pension',Income_From_Salary_Pension_viewset,basename='Income_From_Salary_Pension'),
router.register(r'Income_From_House_Property',Income_From_House_Property_viewset,basename='Income_From_House_Property'),
router.register(r'exempted_income',Income_from_Other_Sources_viewset,basename='Income_from_Other_Sources_viewset'),
router.register(r'Income_from_Business_Services_Profession',Income_from_Business_Services_Profession_viewset,basename='Income_from_Business_Services_Profession'),
router.register(r'Business_of_transport',Business_of_transport_viewset,basename='Business_of_transport'),
router.register(r'Other_Business_viewset',Other_Business_viewset,basename='Other_Business_viewset')
######
router.register(r'itr_products_viewset',itr_products_viewset,basename='itr_products_viewset'),



urlpatterns  = [
    path('',include(router.urls)),
]

