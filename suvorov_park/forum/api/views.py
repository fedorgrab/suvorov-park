from rest_framework.generics import CreateAPIView, ListCreateAPIView

from suvorov_park.forum import models
from suvorov_park.forum.api import serializers


class ForumTopicsListCreateAPIView(ListCreateAPIView):
    queryset = models.ForumTopic.objects.all()
    serializer_class = serializers.ForumTopicSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ForumMessageCreateAPIView(CreateAPIView):
    serializer_class = serializers.ForumMessageSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
