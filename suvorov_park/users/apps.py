from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersAppsConfig(AppConfig):
    name = "suvorov_park.users"
    label = "users"
    verbose_name = _("users")

    def ready(self):
        import suvorov_park.users.password_reset_email  # noqa
