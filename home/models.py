from django.conf import settings
from django.db import models


class App(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=50,
    )
    description = models.CharField(
        max_length=256,
    )
    type = models.CharField(
        max_length=256,
    )
    framework = models.CharField(
        max_length=256,
    )
    domain_name = models.URLField()
    screen_shot = models.URLField()
    subscription = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="app_subscription",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
