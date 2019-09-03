from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ForumAppsConfig(AppConfig):
    name = "suvorov_park.forum"
    label = "forum"
    verbose_name = _("forum")

    def ready(self):
        import suvorov_park.forum.messaging  # noqa
