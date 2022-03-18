from rest_framework import viewsets
from ..models.design import Design
from ..serializers.Design import DesignSerializer

class DesignViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Design.objects.all()
    serializer_class = DesignSerializer