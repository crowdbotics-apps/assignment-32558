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
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="app_user",
    )
    subscription = models.OneToOneField(
        "home.Subscriptions",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="app_subscription",
    )


class Subscriptions(models.Model):
    "Generated Model"
    active = models.BooleanField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    app = models.OneToOneField(
        "home.App",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="subscriptions_app",
    )
    plan = models.OneToOneField(
        "home.Plans",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="subscriptions_plan",
    )
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="subscriptions_user",
    )


class Plans(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=20,
    )
    description = models.CharField(
        max_length=256,
    )
    price = models.DecimalField(
        max_digits=3,
        decimal_places=2,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
