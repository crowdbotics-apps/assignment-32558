from django.conf import settings
from django.db import models


class App(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=50,
    )
    description = models.TextField(blank=True)

    # class _Type(models.TextChoices):

    #     web = "Web", "Web"
    #     mobile = "Mobile", "Mobile"

    TYPE_CHOICES = (
        ("Web", "Web"),
        ("Mobile", "Mobile")
    )

    type = models.TextField(choices=TYPE_CHOICES)

    # class _Frameworks(models.TextChoices):

    #     django = "Django", "Django"
    #     react_native = "React Native", "React Native"

    FW_CHOICES = (
        ("Django", "Django"),
        ("React Native", "React Native")
    )

    framework = models.TextField(choices=FW_CHOICES)
    domain_name = models.CharField(max_length=50, blank=True)
    screen_shot = models.URLField("Screenshot", blank=True, editable=False)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        blank=True,
        related_name="app_user",
        editable=False
    )
    subscription = models.OneToOneField(
        "home.Subscription",
        on_delete=models.DO_NOTHING,
        blank=True,
        related_name="app_subscription",
        editable=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

class Subscription(models.Model):
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
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subscription_app",
    )
    plan = models.OneToOneField(
        "home.Plan",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subscription_plan",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subscription_user",
    )


class Plan(models.Model):
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
