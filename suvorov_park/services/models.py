from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("title"))

    class Meta:
        verbose_name = _("service")
        verbose_name_plural = _("services")

    def __str__(self):
        return self.title


class ServiceOrder(models.Model):
    service = models.ForeignKey(
        to="Service", verbose_name=_("service"), on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, verbose_name=_("user"), on_delete=models.CASCADE
    )
    details = models.CharField(max_length=510, verbose_name=_("details"))
    created_at = models.DateField(auto_now_add=True, verbose_name=_("created_at"))

    class Meta:
        verbose_name = _("order")
        verbose_name_plural = _("orders")
