from rest_framework import viewsets

from .models import *

from .serializers import *

class roc_viewset(viewsets.ModelViewSet):
    queryset = roc.objects.all()
    serializer_class= roc_serializer
