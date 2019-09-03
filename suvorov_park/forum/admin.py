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


@admin.register(models.ForumMessage)
class ForumMessageAdmin(admin.ModelAdmin):
    list_display = ("user", "text", "forum_topic")
    list_select_related = ("forum_topic",)
