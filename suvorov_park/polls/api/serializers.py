from django.db import IntegrityError
from rest_framework import serializers

from suvorov_park.polls import models
from suvorov_park.polls.exceptions import IncorrectPollChoice


class ChoiceSerializer(serializers.ModelSerializer):
    votes = serializers.CharField(read_only=True)
    option = serializers.CharField(source="title")

    class Meta:
        model = models.Choice
        fields = ("id", "option", "votes")


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
    class Meta:
        model = models.Vote
        fields = ()

    def create(self, validated_data):
        try:
            return models.Vote.objects.create(
                user=validated_data["user"],
                poll_id=validated_data["poll_id"],
                choice_id=validated_data["choice_id"],
            )
        except IncorrectPollChoice:
            raise serializers.ValidationError(
                {"detail": "Choice is inappropriate for current poll"}
            )
        except IntegrityError:
            raise serializers.ValidationError(
                {"detail": "Current poll have already been voted by user"}
            )
