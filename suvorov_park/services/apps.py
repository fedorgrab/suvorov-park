from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ServicesAppsConfig(AppConfig):
    name = "suvorov_park.services"
    label = "services"
    verbose_name = _("services")
