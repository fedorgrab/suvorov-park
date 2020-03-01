from django.contrib.auth import authenticate, get_user_model, login, logout
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from suvorov_park.users import models
from . import serializers

User = get_user_model()


class SignInAPIView(GenericAPIView):
    serializer_class = serializers.AuthSerializer
    permission_classes = (~IsAuthenticated,)

    @staticmethod
    def login(request, username, password):
        user = authenticate(request=request, username=username, password=password)
        if not user:
            raise ValidationError({"message": "Invalid credentials"})

        login(request=request, user=user)
        return user

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.login(request=request, **serializer.validated_data)

        if user.is_staff:
            return Response({"user": "admin"})

        return Response({"user": "resident"})


class SignUpAPIView(GenericAPIView):
    serializer_class = serializers.AuthSerializer
    permission_classes = (~IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request=request, user=user)
        return Response(data={"message": "success"})


class SignOutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response(data={"message": "success"})


class PasswordChangeAPIView(GenericAPIView):
    serializer_class = serializers.PasswordChangeSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(
            raw_password=serializer.validated_data["new_password"]
        )
        request.user.save()
        login(request=request, user=request.user)
        return Response(data=dict())


class PasswordResetRequestAPIView(CreateAPIView):
    permission_classes = (~IsAuthenticated,)
    serializer_class = serializers.PasswordResetRequestSerializer

    def post(self, request, *args, **kwargs):
        self.create(request)
        return Response(
            data={
                "detail": _(
                    "Password restore procedure requested successfully: "
                    "Check your email to receive the code and continue "
                    "the next steps"
                )
            }
        )


class PasswordResetConfirmAPIView(GenericAPIView):
    serializer_class = serializers.PasswordResetConfirmSerializer
    permission_classes = (~IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            password_reset_request = models.PasswordResetCode.objects.select_related(
                "user"
            ).get(code=serializer.validated_data["code"])
        except models.PasswordResetCode.DoesNotExist:
            raise ValidationError(
                {"code": [_("Incorrect code: try again or request a new one")]}
            )

        user = password_reset_request.user
        user.set_password(raw_password=serializer.validated_data["new_password"])
        user.save()
        return Response(data={"detail": "Success"})


class UserProfileAPIView(RetrieveAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
