from django.db import models
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    title = models.CharField(max_length=510, verbose_name=_("title"))
    text = models.CharField(max_length=1020, verbose_name=_("text"))
    date = models.DateField(verbose_name=_("date"))

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")
