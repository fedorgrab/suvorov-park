from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PollsAppsConfig(AppConfig):
    name = "suvorov_park.polls"
    label = "polls"
    verbose_name = _("polls")

    def ready(self):
        import suvorov_park.polls.voting  # noqa
