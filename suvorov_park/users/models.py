import secrets

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .exceptions import IncorrectResetEmail


class User(AbstractUser):
    patronymic = models.CharField(
        verbose_name=_("patronymic"), max_length=255, blank=True, null=True
    )
    avatar = models.ImageField(null=True, blank=True, verbose_name=_("avatar"))
    apartment_number = models.SmallIntegerField(
        verbose_name=_("apartment number"), null=True
    )
    apartment_square = models.IntegerField(
        verbose_name=_("apartment square"), null=True
    )

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")


def generate_password_reset_token():
    return secrets.token_hex()


UserModel = get_user_model()


class PasswordResetCodeManager(models.Manager):
    def create(self, email):
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            raise IncorrectResetEmail
        else:
            return super().create(user=user)


class PasswordResetCode(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, verbose_name=_("user"), on_delete=models.CASCADE
    )
    token = models.CharField(
        verbose_name=_("token"),
        unique=True,
        default=generate_password_reset_token,
        max_length=127,
    )
    created_at = models.DateTimeField(verbose_name=_("created_at"), auto_now_add=True)

    objects = PasswordResetCodeManager()

    class Meta:
        verbose_name = _("password reset code")
        verbose_name_plural = _("password reset codes")
