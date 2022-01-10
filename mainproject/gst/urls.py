from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views  import *
router = DefaultRouter()

router.register(r'applygst',apply_for_GST_Registration_viewset,basename='gst'),
router.register(r'gststatus',GST_Status_viewset,basename='tdspersonal'),
router.register(r'gstreturnclientdetails',GST_Return_Client_Details_viewset,basename='gstreturnclientdetails'),
router.register(r'gstselectgst',GST_Return_Select_GST_Type_viewset,basename='selectgstreturn'),
router.register(r'gstreview',view_all_review_gst_form_viewset,basename='gstreview'),


#####

router.register(r'gst_products',gst_products_viewset,basename='gst_products'),






urlpatterns  = [
    path('',include(router.urls)),
]