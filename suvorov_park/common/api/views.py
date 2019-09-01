from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from suvorov_park.common import models
from suvorov_park.common.api import serializers


class NewsListAPIView(ListAPIView):
    serializer_class = serializers.NewsSerializer
    queryset = models.News.objects.all()
    permission_classes = (IsAuthenticated,)
