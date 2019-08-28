from django.contrib.auth import authenticate, login, logout
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AuthSerializer


class SignInAPIView(GenericAPIView):
    serializer_class = AuthSerializer
    permission_classes = (~IsAuthenticated,)

    @staticmethod
    def login(request, username, password):
        user = authenticate(request=request, username=username, password=password)
        if not user:
            raise ValidationError({"message": "Invalid credendials"})

        login(request=request, user=user)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.login(request=request, **serializer.validated_data)
        return Response({"message": "success"})


class SignUpAPIView(GenericAPIView):
    serializer_class = AuthSerializer
    permission_classes = (~IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request=request, user=user)
        return Response(data={})


class SignOutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({"message": "success"})
