from django.contrib import admin

from suvorov_park.services import models


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(models.ServiceOrder)
class ServiceOrderAdmin(admin.ModelAdmin):
    list_display = ("user", "service", "details", "created_at")
    list_select_related = ("user", "service")
    list_filter = ("service", "created_at")
    search_fields = ("details", "user")
