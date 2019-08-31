from rest_framework import serializers

from suvorov_park.common.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("id", "title", "text", "date")
