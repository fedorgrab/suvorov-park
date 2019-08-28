from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


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
