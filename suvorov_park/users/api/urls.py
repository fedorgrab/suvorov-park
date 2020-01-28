from django.urls import path

from . import views

app_name = "users"

# fmt: off
urlpatterns = [
    path("sign-in", views.SignInAPIView.as_view(), name="sign-in"),
    path("sign-up", views.SignUpAPIView.as_view(), name="sign-up"),
    path("sign-out", views.SignOutAPIView.as_view(), name="sign-out"),
    path("password-change", views.PasswordChangeAPIView.as_view(), name="password-change"),
    path("password-reset-request", views.PasswordResetRequestAPIView.as_view(), name="password-reset-request"),
    path("password-reset-confirm", views.PasswordResetConfirmAPIView.as_view(), name="password-reset-confirm"),
]
# fmt: on
