from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from suvorov_park.polls.models import Choice, UserChoice


def vote(choice_id):
    Choice.objects.filter(id=choice_id).update(votes=models.F("votes") + 1)


@receiver(pre_save, sender=UserChoice)
def vote_for_poll_choice(sender, instance, **kwargs):
    vote(instance.choice_id)
