from rest_framework import viewsets, mixins, parsers, renderers
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from permission.permission import UpdateUserPermission
from .serializers import UserSerializer, PhoneSerializer
from .models import User

import random

# User-related ViewSet--------------------------------------------------------------------------------------------------
class UserViewSet(
            mixins.CreateModelMixin,
            mixins.ListModelMixin,
            mixins.UpdateModelMixin,
            mixins.DestroyModelMixin,
            mixins.RetrieveModelMixin,
            viewsets.GenericViewSet
            ):

    authentication_classes = [JWTAuthentication]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]

        elif self.action == 'list':
            return [IsAdminUser()]

        return [UpdateUserPermission()]


# Login-related ViewSet-------------------------------------------------------------------------------------------------

def send_sms_to_user(phone_number):
    code = ""
    for _ in range(6):
        random_digit = str(random.randint(0, 9))
        code += random_digit

    return code


class LoginStepOneAPIView(GenericAPIView):
    serializer_class = PhoneSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        phone_number = request.data['phone']
        code = send_sms_to_user(phone_number=phone_number)

        if serializer.is_valid(raise_exception=True):
            return Response({"code": code})





