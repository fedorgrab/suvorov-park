from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from suvorov_park.mailing import send_mailing
from suvorov_park.users.models import PasswordResetCode


@receiver(post_save, sender=PasswordResetCode)
def send_code_email(sender, instance, *args, **kwargs):
    send_mailing(
        users=[instance.user],
        subject=_("Password reset code"),
        mail_template="emails/password_reset.html",
        mail_object=instance,
    )
