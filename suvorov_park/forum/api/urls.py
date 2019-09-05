from django.urls import path

from suvorov_park.forum.api import views

urlpatterns = [
    path("", views.ForumTopicsListCreateAPIView.as_view(), name="forum_topics"),
    path(
        "<forum_topic_id>/message",
        views.ForumMessageCreateAPIView.as_view(),
        name="message",
    ),
]
