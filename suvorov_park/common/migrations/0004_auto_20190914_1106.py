# Generated by Django 2.2.4 on 2019-09-14 08:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("common", "0003_auto_20190903_2250"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="sitesetting",
            options={
                "verbose_name": "Site setting",
                "verbose_name_plural": "Site settings",
            },
        ),
        migrations.AlterField(
            model_name="news",
            name="text",
            field=models.TextField(max_length=1020, verbose_name="text"),
        ),
        migrations.AlterField(
            model_name="settingimage",
            name="image_file",
            field=models.ImageField(
                upload_to="common/images", verbose_name="image file"
            ),
        ),
        migrations.AlterField(
            model_name="settingvideo",
            name="video_file",
            field=models.FileField(
                upload_to="common/videos", verbose_name="video file"
            ),
        ),
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=255, null=True, verbose_name="email"
                    ),
                ),
                ("text", models.CharField(max_length=1020, verbose_name="text")),
                (
                    "created_at",
                    models.DateField(auto_now_add=True, verbose_name="created_at"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={"verbose_name": "Feedback", "verbose_name_plural": "Feedback"},
        ),
    ]
