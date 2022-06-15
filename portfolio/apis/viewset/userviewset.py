


from rest_framework import viewsets
from ..models.user import User
from ..serializers.User import UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer