from django.contrib import admin
from django.urls import include, path
from django.utils.translation import gettext_lazy as _

app_name = "suvorov_park"

urlpatterns = [
    path("users/", include("suvorov_park.users.api.urls")),
    path("common/", include("suvorov_park.common.api.urls")),
]

admin.site.site_header = _("Suvorov park Admin")
