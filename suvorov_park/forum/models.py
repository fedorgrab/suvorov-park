from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class ForumTopic(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("title"))
    number_of_messages = models.IntegerField(
        verbose_name=_("number of comments"), default=0
    )
    number_of_members = models.IntegerField(
        verbose_name=_("number of members"), default=1
    )
    created_at = models.DateField(verbose_name=_("created_at"), auto_now_add=True)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, verbose_name=_("author"), on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _("forum topic")
        verbose_name_plural = _("forum topics")


class ForumMessage(models.Model):
    text = models.CharField(max_length=255, verbose_name=_("text"))
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, verbose_name=_("user"), on_delete=models.CASCADE
    )
    forum_topic = models.ForeignKey(
        to="ForumTopic",
        verbose_name=_("forum topic"),
        on_delete=models.CASCADE,
        related_name="messages",
    )

    class Meta:
        verbose_name = _("forum message")
        verbose_name_plural = _("forum messages")
