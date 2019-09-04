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
