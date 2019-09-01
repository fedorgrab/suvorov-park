from django.urls import path

from suvorov_park.common.api import views

app_name = "common"

urlpatterns = [path("news", views.NewsListAPIView.as_view(), name="news")]
