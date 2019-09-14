from rest_framework import serializers

from suvorov_park.common import models


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = ("id", "title", "text", "date")


class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    email = serializers.EmailField(allow_null=True, required=False)

    class Meta:
        model = models.Feedback
        fields = ("name", "email", "user", "text")

    def create(self, validated_data):
        email, user = validated_data.get("email"), validated_data.get("user")

        if not (email or user):
            raise serializers.ValidationError(
                {"detail": "Either email or credentials should be provided"}
            )

        return models.Feedback.objects.create(**validated_data)


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
