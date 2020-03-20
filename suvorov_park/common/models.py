from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel


class SiteSetting(SingletonModel):
    about = models.TextField(verbose_name=_("about"))

    class Meta:
        verbose_name = _("Site setting")
        verbose_name_plural = _("Site settings")


class SettingImage(models.Model):
    setting = models.ForeignKey(
        to="SiteSetting",
        on_delete=models.CASCADE,
        verbose_name=_("setting"),
        related_name="images",
    )
    image_file = models.ImageField(
        upload_to="common/images", verbose_name=_("image file")
    )

    def __str__(self):
        return ""

    class Meta:
        verbose_name = _("setting image")
        verbose_name_plural = _("setting images")


class SettingVideo(models.Model):
    setting = models.ForeignKey(
        to="SiteSetting",
        on_delete=models.CASCADE,
        verbose_name=_("settings"),
        related_name="videos",
    )
    video_file = models.FileField(
        upload_to="common/videos", verbose_name=_("video file")
    )

    class Meta:
        verbose_name = _("setting video")
        verbose_name_plural = _("setting videos")

    def __str__(self):
        return ""


class News(models.Model):
    title = models.CharField(max_length=510, verbose_name=_("title"))
    text = models.TextField(max_length=1020, verbose_name=_("text"))
    date = models.DateField(verbose_name=_("date"))

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")

    def __str__(self):
        return self.title


class Feedback(models.Model):
    PROCESSED = "processed"
    IN_PROGRESS = "in progress"
    MODERATION_STATUSES = ((PROCESSED, _("processed")), (IN_PROGRESS, _("in progress")))

    name = models.CharField(verbose_name=_("name"), max_length=255)
    email = models.EmailField(
        verbose_name=_("email"), max_length=255, null=True, blank=True
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("user"),
        null=True,
        blank=True,
    )
    # text = models.CharField(max_length=1020, verbose_name=_("text"))
    text = models.TextField(verbose_name=_("text"))
    created_at = models.DateField(verbose_name=_("created_at"), auto_now_add=True)
    status = models.CharField(
        max_length=127,
        verbose_name=_("status"),
        choices=MODERATION_STATUSES,
        default=IN_PROGRESS,
    )

    class Meta:
        verbose_name = _("Feedback")
        verbose_name_plural = _("Feedback")
