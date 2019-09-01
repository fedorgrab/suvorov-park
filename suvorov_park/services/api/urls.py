from django.urls import path

from suvorov_park.services.api import views

urlpatterns = [
    path("", views.ServiceListAPIView.as_view(), name="services"),
    path("<str:service_id>/order", views.ServiceOrderAPIView.as_view(), name="order"),
]
