from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'tdsclient',tds_client_view,basename='tdsclient'),
router.register(r'searchtds',search_tds_view,basename='tdspersonal'),
router.register(r'tdsbusiness',search_tds_business_view,basename='tdsbusiness'),
router.register(r'order',order_enquiry_view,basename='tdsenquiry'),
#####
router.register(r'tds_or_tcs_products',tds_or_tcs_products_view,basename='tds_or_tcs_products'),


urlpatterns = [
    path('',include(router.urls)),
]