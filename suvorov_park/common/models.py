from django.db import models
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel


class SiteSetting(SingletonModel):
    saved = models.BooleanField(
        default=True
    )  # this is a flag for index out of range   Error
    about = models.TextField(verbose_name=_("about"))


class SettingMedia(models.Model):
    setting = models.ForeignKey(
        to="SiteSetting", on_delete=models.CASCADE, verbose_name=_("setting")
    )
    media_file = models.FileField()

    def __str__(self):
        return "медиа файл конфигурации сайта"

    class Meta:
        verbose_name = _("setting")


class News(models.Model):
    title = models.CharField(max_length=510, verbose_name=_("title"))
    text = models.CharField(max_length=1020, verbose_name=_("text"))
    date = models.DateField(verbose_name=_("date"))

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")
