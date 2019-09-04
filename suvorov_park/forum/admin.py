from django.contrib import admin

from suvorov_park.forum import models


@admin.register(models.ForumTopic)
class ForumTopicAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "number_of_messages",
        "number_of_members",
        "created_at",
        "author",
    )
    list_filter = ("created_at", "author")
    search_fields = ("title", "author")


@admin.register(models.ForumMessage)
class ForumMessageAdmin(admin.ModelAdmin):
    list_display = ("user", "text", "forum_topic")
    list_select_related = ("forum_topic",)
    search_fields = ("text", "forum_topic")
