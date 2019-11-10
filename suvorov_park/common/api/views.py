from django.contrib.auth.models import AnonymousUser
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from suvorov_park.common import models
from suvorov_park.common.api import serializers


class NewsListAPIView(ListAPIView):
    serializer_class = serializers.NewsSerializer
    queryset = models.News.objects.all().order_by("-id")
    permission_classes = (IsAuthenticated,)


class SettingAPIView(RetrieveAPIView):
    serializer_class = serializers.SiteSettingSerializer

    def get_object(self):
        return models.SiteSetting.objects.get()


class FeedbackCreateAPIView(CreateAPIView):
    serializer_class = serializers.FeedbackSerializer

    def perform_create(self, serializer):
        if not isinstance(self.request.user, AnonymousUser):
            serializer.save(user=self.request.user)

        super().perform_create(serializer)
