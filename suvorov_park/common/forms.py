from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class SendEmailToUsersForm(forms.Form):
    users = forms.ModelMultipleChoiceField(
        label="Выбор пользователей",
        queryset=User.objects.filter(is_staff=False),
        widget=forms.SelectMultiple(attrs={"class": "select_inner"}),
        required=False,
    )
    send_to_all = forms.BooleanField(label="отправить всем", required=False)
