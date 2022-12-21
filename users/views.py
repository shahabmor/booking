from rest_framework import viewsets, mixins, parsers, renderers
from .serializers import UserSerializer
from .models import User


class UserViewSet(
            mixins.CreateModelMixin,
            mixins.ListModelMixin,
            mixins.UpdateModelMixin,
            mixins.DestroyModelMixin,
            mixins.RetrieveModelMixin,
            viewsets.GenericViewSet
            ):

    queryset = User.objects.all()
    serializer_class = UserSerializer





