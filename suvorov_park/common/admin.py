from django.contrib import admin, messages
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path, reverse
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from solo.admin import SingletonModelAdmin

from suvorov_park.mailing import send_mailing
from . import forms, models

User = get_user_model()

# Email sending success messages
SUCCESS_MESSAGE_OPT_1_FORMAT = _(
    "Поздравляем! Только что вы добавили новую новость на сайт ТСЖ Суворов-Парк.<br> "
    "Оповещение о новости получат {0} пользователей."
)
SUCCESS_MESSAGE_OPT_2_FORMAT = _(
    "Поздравляем! Только что вы добавили новую новость на сайт ТСЖ Суворов-Парк.<br> "
    "Оповещение о новости получат {0} из выбранных вами "
    "{1} пользователей. "
)
SUCCESS_MESSAGE_OPT_2_WARNING = _(
    "Примечание: не все выбранные пользователи получат рассылку, "
    "так как не у всех заполнен email в личном кабинете. Обратитесь к пользователю для "
    "заполнения его электронной почты."
)
SUCCESS_FEEDBACK_EMAIL_ANSWER = _(
    "Поздравляем! Вы ответили на одну заявку обратной свзязи! <br>"
    'Не волнуйтесь, теперь эта заявка будет в нижней части списка и помечена маркером "обработан"'
)

NEWS_OBJECT = None


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    list_filter = ("date",)
    search_fields = ("title", "text")

    def get_urls(self):
        urlpatterns = super().get_urls()
        app_label, model_name = self.model._meta.app_label, self.model._meta.model_name

        return [
            path(
                "send-emails/",
                self.send_emails_view,
                name=f"{app_label}_{model_name}_send_emails",
            ),
            *urlpatterns,
        ]

    def response_post_save_add(self, request, obj):
        form = forms.SendEmailToUsersForm(request.POST)

        if form.is_valid():
            global NEWS_OBJECT
            NEWS_OBJECT = obj

            return render(
                request=request,
                template_name="admin/email_sending.html",
                context={"form": form, **admin.site.each_context(request)},
            )

    def send_emails_view(self, request):
        form = forms.SendEmailToUsersForm(request.POST)
        form.is_valid()

        if "apply" in request.POST:
            users = form.cleaned_data["users"]
            send_to_all = form.cleaned_data["send_to_all"]

            if send_to_all:
                users_id = users.values_list("id", flat=True)
                users = User.objects.filter(is_staff=False).exclude(id__in=users_id)

            users_with_emails = users.exclude(email__exact="", email__isnull=False)

            send_mailing(
                users=users_with_emails,
                subject=_("News"),
                mail_template="emails/news_email.html",
                mail_object=NEWS_OBJECT,
            )

            number_of_total_users = users.count()
            number_of_processed_users = users_with_emails.count()

            if number_of_total_users == number_of_processed_users:
                success_msg_1 = SUCCESS_MESSAGE_OPT_1_FORMAT.format(
                    number_of_processed_users
                )
                self.message_user(
                    request, mark_safe(success_msg_1), level=messages.SUCCESS
                )
            else:
                success_msg_2 = SUCCESS_MESSAGE_OPT_2_FORMAT.format(
                    number_of_total_users, number_of_processed_users
                )
                self.message_user(
                    request, mark_safe(success_msg_2), level=messages.SUCCESS
                )
                self.message_user(
                    request,
                    mark_safe(SUCCESS_MESSAGE_OPT_2_WARNING),
                    level=messages.WARNING,
                )

        return HttpResponseRedirect(reverse("admin:common_news_changelist"))


class ImageInline(admin.StackedInline):
    model = models.SettingImage
    extra = 0


class VideoInline(admin.StackedInline):
    model = models.SettingVideo
    extra = 0


@admin.register(models.SiteSetting)
class SettingAdmin(SingletonModelAdmin):
    inlines = (ImageInline, VideoInline)


@admin.register(models.Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_select_related = ("user",)
    list_display = (
        "user",
        "name",
        "text",
        "status",
        "created_at",
        "send_feedback_answer_email_button",
    )
    readonly_fields = ("user", "email", "name", "created_at", "text")
    list_editable = ("status",)
    ordering = ("status", "-created_at")
    button_style = (
        "background: #4b505f; border-radius: 3px; color: white; padding: 5px 15px"
    )

    def suit_row_attributes(self, obj, request):
        css_class = {"processed": "success", "in progress": "warning"}.get(obj.status)

        return {"class": css_class, "data": obj.name}

    def get_urls(self):
        # fmt: off
        return [path(
            "<int:feedback_id>/send-email",
            self.admin_site.admin_view(self.send_email),
            name="send_feedback_answer_email"
        )] + super().get_urls()
        # fmt: on

    def send_feedback_answer_email_button(self, obj):
        return mark_safe(
            "<a style='{}' href='{}'>Ответить</a>".format(
                self.button_style,
                reverse("admin:send_feedback_answer_email", args=[obj.pk]),
            )
        )

    send_feedback_answer_email_button.short_description = _("Answer")

    def send_email(self, request, feedback_id):
        form = forms.AnswerFeedbackEmailForm(request.POST)
        form.is_valid()
        feedback = models.Feedback.objects.select_related("user").get(id=feedback_id)

        if "apply" in request.POST:
            text = form.cleaned_data["text"]
            setattr(feedback, "answer_text", text)

            if feedback.email:
                send_mailing(
                    email_addresses=[feedback.email],
                    subject=_("Feedback"),
                    mail_template="emails/feedback_answer.html",
                    mail_object=feedback,
                )
            else:
                send_mailing(
                    users=[feedback.user],
                    subject=_("Feedback"),
                    mail_template="emails/feedback_answer.html",
                    mail_object=feedback,
                )

            feedback.status = models.Feedback.PROCESSED
            feedback.save()

            self.message_user(
                request=request,
                message=mark_safe(SUCCESS_FEEDBACK_EMAIL_ANSWER),
                level=messages.SUCCESS,
            )
            return HttpResponseRedirect(reverse("admin:common_feedback_changelist"))

        return render(
            request,
            "admin/feedback_answer_email.html",
            context={"form": form, "obj": feedback, **admin.site.each_context(request)},
        )
