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
    
    def __str__(self):
        return self.name


class Subscription(models.Model):
    "Generated Model"

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="subscription_user",
        editable=False
    )

    plan = models.OneToOneField(
        "home.Plan",
        on_delete=models.CASCADE,
        related_name="subscription_plan",
    )

    app = models.OneToOneField(
        "home.App",
        on_delete=models.CASCADE,
        related_name="subscription_app",
    )

    active = models.BooleanField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )


class Plan(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=20,
    )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.name} ({self.price})"
