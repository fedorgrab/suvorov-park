from django.urls import path

from . import views

urlpatterns = [
    path("", views.PollListCreateAPIView.as_view(), name="polls"),
    path(
        "<str:poll_id>/vote/<str:choice_id>", views.VoteAPIView.as_view(), name="vote"
    ),
]
