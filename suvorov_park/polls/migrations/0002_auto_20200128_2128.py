# Generated by Django 2.2.4 on 2020-01-28 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("polls", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="vote",
            name="choice",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_votes",
                to="polls.Choice",
                verbose_name="choice",
            ),
        ),
        migrations.AlterField(
            model_name="vote",
            name="poll",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_votes",
                to="polls.Poll",
                verbose_name="poll",
            ),
        ),
    ]
