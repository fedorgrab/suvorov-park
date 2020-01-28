from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from suvorov_park.users.exceptions import IncorrectResetEmail
from suvorov_park.users.models import PasswordResetCode

User = get_user_model()


def validate_password(value):
    regex_validate = RegexValidator(
        regex=r"^(?=.*\d).{8,}",
        message=_("Invalid password: it should have numeric symbols"),
    )
    return regex_validate(value)


class AuthSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(required=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = ("username", "password")

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class PasswordChangeSerializer(serializers.Serializer):
    new_password = serializers.CharField(
        required=True,
        style={"input_type": "password"},
        help_text="Password should be typed twice and validated on frontend",
    )


class PasswordResetRequestSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = PasswordResetCode
        fields = ("email",)

    def create(self, validated_data):
        try:
            return PasswordResetCode.objects.create(**validated_data)
        except IncorrectResetEmail:
            raise serializers.ValidationError(
                {"detail": "Provided email was not found in the database"}
            )


class PasswordResetConfirmSerializer(serializers.Serializer):
    code = serializers.IntegerField(help_text="Code that user received via email")
    new_password = serializers.CharField(
        style={"input_type": "password"},
        help_text="Password should be typed twice and validated on frontend",
    )
