from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from suvorov_park.services import models
from suvorov_park.services.api import serializers


class ServiceListAPIView(ListAPIView):
    serializer_class = serializers.ServiceSerializer
    queryset = models.Service.objects.all()
    permission_classes = (IsAuthenticated,)


class ServiceOrderAPIView(CreateAPIView):
    serializer_class = serializers.ServiceOrderSerializer
    permission_classes = (IsAuthenticated,)
    service_id_url_kwarg = "service_id"

    def perform_create(self, serializer):
        service_id = self.kwargs[self.service_id_url_kwarg]
        serializer.save(user=self.request.user, service_id=service_id)
