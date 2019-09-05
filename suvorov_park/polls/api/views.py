from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from suvorov_park.polls import models
from . import serializers


class PollListCreateAPIView(ListCreateAPIView):
    queryset = (
        models.Poll.objects.all().prefetch_related("choices").select_related("owner")
    )
    serializer_class = serializers.PollSerializer
    permission_classes = (IsAuthenticated,)

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

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        serializer.save(user=self.request.user, choice_id=choice_id, poll_id=poll_id)

        poll_instance = models.Poll.objects.get(id=poll_id)
        poll_serializer = serializers.PollSerializer(poll_instance)
        return Response(poll_serializer.data)
