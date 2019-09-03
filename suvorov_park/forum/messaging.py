from django.db.models import F
from django.db.models.signals import pre_save
from django.dispatch import receiver

from suvorov_park.forum.models import ForumMessage, ForumTopic


def message_forum_topic(forum_topic, user):
    update_kwargs = {"number_of_messages": F("number_of_messages") + 1}

    if not ForumMessage.objects.filter(forum_topic_id=forum_topic, user=user).exists():
        update_kwargs.update(number_of_members=F("number_of_members") + 1)

    ForumTopic.objects.filter(id=forum_topic.id).update(**update_kwargs)


@receiver(pre_save, sender=ForumMessage)
def message_on_forum(sender, instance, **kwargs):
    message_forum_topic(forum_topic=instance.forum_topic, user=instance.user)
