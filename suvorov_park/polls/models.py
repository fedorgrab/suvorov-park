from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Poll(models.Model):
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("owner")
    )
    title = models.CharField(max_length=255, verbose_name=_("title"))
    created_at = models.DateField(verbose_name=_("created_at"), auto_now_add=True)

    class Meta:
        verbose_name = _("poll")
        verbose_name_plural = _("polls")

    def __str__(self):
        return self.title


class Choice(models.Model):
    poll = models.ForeignKey(
        to="Poll",
        on_delete=models.CASCADE,
        verbose_name=_("poll"),
        related_name="choices",
    )
    title = models.CharField(max_length=255, verbose_name=_("title"))
    votes = models.IntegerField(default=0, verbose_name=_("votes"))

    class Meta:
        verbose_name = _("choice")
        verbose_name_plural = _("choices")
        constraints = (
            models.UniqueConstraint(fields=("title", "poll"), name="poll_title_unique"),
        )

    def __str__(self):
        return ""


class Vote(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, verbose_name=_("user"), on_delete=models.CASCADE
    )
    poll = models.ForeignKey(
        to="Poll", verbose_name=_("poll"), on_delete=models.CASCADE
    )
    choice = models.ForeignKey(
        to="Choice", verbose_name=_("choice"), on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _("vote")
        verbose_name_plural = _("votes")
        db_table = "polls_userchoice"
        constraints = (
            models.UniqueConstraint(fields=("poll", "user"), name="unique_vote"),
        )
