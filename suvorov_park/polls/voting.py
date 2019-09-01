from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from suvorov_park.polls.exceptions import IncorrectPollChoice
from suvorov_park.polls.models import Choice, Vote


def vote(choice_id, poll_id):
    updated = Choice.objects.filter(id=choice_id, poll_id=poll_id).update(
        votes=models.F("votes") + 1
    )

    if not updated:
        raise IncorrectPollChoice


@receiver(pre_save, sender=Vote)
def vote_for_poll_choice(sender, instance, **kwargs):
    vote(choice_id=instance.choice_id, poll_id=instance.poll_id)
