from django.contrib import admin
from solo.admin import SingletonModelAdmin

from . import models


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "date")


class MediaInline(admin.TabularInline):
    model = models.SettingMedia
    extra = 0


@admin.register(models.SiteSetting)
class SettingAdmin(SingletonModelAdmin):
    inlines = (MediaInline,)
