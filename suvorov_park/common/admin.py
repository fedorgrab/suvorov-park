from django.contrib import admin
from solo.admin import SingletonModelAdmin

from . import models


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    list_filter = ("date",)
    search_fields = ("title", "text")


class ImageInline(admin.TabularInline):
    model = models.SettingImage
    extra = 0


class VideoInline(admin.TabularInline):
    model = models.SettingVideo
    extra = 0


@admin.register(models.SiteSetting)
class SettingAdmin(SingletonModelAdmin):
    inlines = (ImageInline, VideoInline)
