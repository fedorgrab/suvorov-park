from rest_framework import serializers

from suvorov_park.forum import models


class ForumMessageSerializer(serializers.ModelSerializer):
    forum_topic = serializers.PrimaryKeyRelatedField(
        queryset=models.ForumTopic.objects.all()
    )

    class Meta:
        model = models.ForumMessage
        fields = ("text", "forum_topic")

    def create(self, validated_data):
        return models.ForumMessage.objects.create(
            user=validated_data["user"],
            text=validated_data["text"],
            forum_topic=validated_data["forum_topic"],
        )


class ForumTopicSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    number_of_messages = serializers.IntegerField(read_only=True)
    number_of_members = serializers.IntegerField(read_only=True)
    messages = ForumMessageSerializer(many=True, read_only=True)

    class Meta:
        model = models.ForumTopic
        fields = "__all__"

    def create(self, validated_data):
        return models.ForumTopic.objects.create(
            title=validated_data["title"], author=validated_data["user"]
        )
