from django.urls import path

from .views import NewsListAPIView

app_name = "common"

urlpatterns = [path("news", NewsListAPIView.as_view(), name="news")]
