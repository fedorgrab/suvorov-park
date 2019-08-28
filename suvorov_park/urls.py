from django.contrib import admin
from django.utils.translation import gettext_lazy as _

app_name = "suvorov_park"

urlpatterns = []

admin.site.site_header = _("Suvorov park Admin")
