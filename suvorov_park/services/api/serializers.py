from rest_framework import serializers

from suvorov_park.services import models


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = ("id", "title")


class ServiceOrderSerializer(serializers.ModelSerializer):
    service = serializers.CharField(read_only=True)

    class Meta:
        model = models.ServiceOrder
        fields = ("details", "service")

    def create(self, validated_data):
        return models.ServiceOrder.objects.create(
            user=validated_data["user"],
            service_id=validated_data["service_id"],
            details=validated_data["details"],
        )
