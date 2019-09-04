from rest_framework import serializers

from suvorov_park.common import models


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = ("id", "title", "text", "date")


class ImageSettingSerializer(serializers.ModelSerializer):
    url = serializers.URLField(source="image_file.url")

    class Meta:
        model = models.SettingImage
        fields = ("url",)


class VideoSettingSerializer(serializers.ModelSerializer):
    url = serializers.URLField(source="vide_file.url")

    class Meta:
        model = models.SettingVideo
        fields = ("url",)


class SiteSettingSerializer(serializers.ModelSerializer):
    images = ImageSettingSerializer(many=True)
    videos = VideoSettingSerializer(many=True)

    class Meta:
        model = models.SiteSetting
        fields = ("about", "images", "videos")
