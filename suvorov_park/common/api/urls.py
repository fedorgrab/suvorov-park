from django.urls import path

from suvorov_park.common.api import views

app_name = "common"

urlpatterns = [
    path("general-configuration", views.SettingAPIView.as_view(), name="genera_config"),
    path("news", views.NewsListAPIView.as_view(), name="news"),
    path("feedback", views.FeedbackCreateAPIView.as_view(), name="feedback_create"),
]
