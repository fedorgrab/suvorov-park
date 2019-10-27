from django.db.models import OuterRef, Subquery
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from suvorov_park.polls import models
from . import serializers


class PollListCreateAPIView(ListCreateAPIView):
    serializer_class = serializers.PollSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user_votes = models.Vote.objects.filter(
            user=self.request.user, poll_id=OuterRef("id")
        )
        return (
            models.Poll.objects.prefetch_related("choices")
            .annotate(user_voted_for=Subquery(user_votes.values("choice__title")[:1]))
            .order_by("-id")
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VoteAPIView(GenericAPIView):
    poll_id_url_kwarg = "poll_id"
    choice_id_url_kwarg = "choice_id"
    serializer_class = serializers.VoteSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        choice_id = self.kwargs[self.choice_id_url_kwarg]
        poll_id = self.kwargs[self.poll_id_url_kwarg]

        vote_serializer = self.get_serializer(data=request.data)
        vote_serializer.is_valid()
        vote_serializer.save(
            user=self.request.user, choice_id=choice_id, poll_id=poll_id
        )

        user_votes = models.Vote.objects.filter(
            user=self.request.user, poll_id=OuterRef("id")
        )
        poll_instance = models.Poll.objects.annotate(
            user_voted_for=Subquery(user_votes.values("choice__title")[:1])
        ).get(id=poll_id)

        poll_serializer = serializers.PollSerializer(poll_instance)
        return Response(poll_serializer.data)
