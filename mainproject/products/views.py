
from rest_framework import viewsets

from .models import *

from .serializers import *

class products_viewset(viewsets.ModelViewSet):
    queryset = products.objects.all()
    serializer_class= products_serializer
