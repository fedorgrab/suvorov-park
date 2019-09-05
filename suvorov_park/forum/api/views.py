from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from suvorov_park.forum import models
from suvorov_park.forum.api import serializers


class ForumTopicsListCreateAPIView(ListCreateAPIView):
    queryset = (
        models.ForumTopic.objects.all()
        .select_related("author")
        .prefetch_related("messages")
    )
    serializer_class = serializers.ForumTopicSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ForumMessageCreateAPIView(CreateAPIView):
    serializer_class = serializers.ForumMessageSerializer
    lookup_url_kwarg = "forum_topic_id"
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        forum_topic_id = self.kwargs[self.lookup_url_kwarg]
        serializer.save(user=self.request.user, forum_topic_id=forum_topic_id)
