from rest_framework import serializers

from suvorov_park.forum import models


class ForumMessageSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = models.ForumMessage
        fields = ("text", "user")


class ForumTopicSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True, source="author")
    number_of_messages = serializers.IntegerField(read_only=True)
    number_of_members = serializers.IntegerField(read_only=True)
    messages = ForumMessageSerializer(many=True, read_only=True)

    class Meta:
        model = models.ForumTopic
        fields = (
            "title",
            "user",
            "number_of_messages",
            "number_of_members",
            "messages",
        )


class ForumTopicShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ForumTopic
        fields = ("id", "title")
