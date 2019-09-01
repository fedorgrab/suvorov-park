from rest_framework import serializers

from suvorov_park.common import models


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = ("id", "title", "text", "date")
