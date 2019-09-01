from django.contrib import admin

from . import models


class ChoiceInline(admin.TabularInline):
    model = models.Choice
    can_delete = False
    extra = 0
    readonly_fields = ("title", "votes")


@admin.register(models.Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "created_at")
    inlines = (ChoiceInline,)
    list_select_related = ("owner",)


@admin.register(models.Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("title", "votes")
    list_select_related = ("poll",)


@admin.register(models.Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ("user", "choice")
    list_select_related = ("user", "choice", "poll")
