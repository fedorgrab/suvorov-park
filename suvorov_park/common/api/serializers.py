from rest_framework import serializers

from suvorov_park.common import models


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = ("id", "title", "text", "date")


class SiteSettingSerializer(serializers.ModelSerializer):
    videos = serializers.StringRelatedField(many=True)
    images = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.SiteSetting
        fields = ("about", "images", "videos")
