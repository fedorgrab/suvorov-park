from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from suvorov_park.polls import models


class ChoiceSerializer(serializers.ModelSerializer):
    votes = serializers.CharField(read_only=True)

    class Meta:
        model = models.Choice
        fields = ("id", "title", "votes")


class PollSerializer(serializers.ModelSerializer):
    title = serializers.CharField(help_text="string")
    choices = ChoiceSerializer(many=True, help_text='[{"title": string}]')
    owner = serializers.CharField(read_only=True)

    class Meta:
        model = models.Poll
        fields = ("id", "owner", "title", "created_at", "choices")

    def create(self, validated_data):
        choice_titles = map(lambda x: x["title"], validated_data["choices"])
        poll = models.Poll.objects.create(
            title=validated_data["title"], owner=validated_data["user"]
        )
        choices = [models.Choice(poll=poll, title=title) for title in choice_titles]
        models.Choice.objects.bulk_create(objs=choices)
        return poll


class VoteSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    poll = serializers.CharField(read_only=True)
    choice = serializers.CharField(read_only=True)

    class Meta:
        model = models.UserChoice
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=models.UserChoice.objects.all(), fields=("user", "poll")
            )
        ]

    def create(self, validated_data):
        return models.UserChoice.objects.create(
            user=validated_data["user"],
            poll_id=validated_data["poll_id"],
            choice_id=validated_data["choice_id"],
        )
