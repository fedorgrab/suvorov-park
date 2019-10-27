from django.conf import settings
from django.contrib.auth import get_user_model
from django.core import mail
from django.template.loader import render_to_string

User = get_user_model()


def send_mailing(users, subject, mail_template, mail_object):
    emails = []
    for user in users:
        html_msg = render_to_string(
            mail_template,
            context={"obj": mail_object, "user": user, "base_url": settings.BASE_URL},
        )
        email = mail.message.EmailMessage(
            subject=subject, body=html_msg, to=[user.email]
        )
        email.content_subtype = "html"
        emails.append(email)

    connection = mail.get_connection()
    connection.send_messages(emails)
    connection.close()
