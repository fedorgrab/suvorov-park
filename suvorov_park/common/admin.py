from django.contrib import admin
from solo.admin import SingletonModelAdmin

from . import models


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    list_filter = ("date",)
    search_fields = ("title", "text")


class ImageInline(admin.StackedInline):
    model = models.SettingImage
    extra = 0


class VideoInline(admin.StackedInline):
    model = models.SettingVideo
    extra = 0


@admin.register(models.SiteSetting)
class SettingAdmin(SingletonModelAdmin):
    inlines = (ImageInline, VideoInline)


@admin.register(models.Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_select_related = ("user",)
    list_display = ("user", "email", "name", "status", "created_at")
    list_editable = ("status",)
    ordering = ("-created_at",)

    def suit_row_attributes(self, obj, request):
        css_class = {"processed": "success", "in progress": "warning"}.get(obj.status)

        return {"class": css_class, "data": obj.name}
