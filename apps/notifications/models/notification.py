from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.base import BaseModel


class Notification(BaseModel):
    """
    User notification.
    """

    class Type(models.TextChoices):
        SYSTEM = "system", _("System")
        ORDER = "order", _("Order")
        PAYMENT = "payment", _("Payment")
        PROMOTION = "promotion", _("Promotion")

    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="notifications",
        verbose_name=_("User"),
    )

    title = models.CharField(
        max_length=255,
        verbose_name=_("Title"),
    )

    message = models.TextField(
        verbose_name=_("Message"),
    )

    notification_type = models.CharField(
        max_length=20,
        choices=Type.choices,
        verbose_name=_("Notification Type"),
    )

    is_read = models.BooleanField(
        default=False,
        verbose_name=_("Is Read"),
    )

    read_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Read At"),
    )

    class Meta:
        db_table = "notifications"
        ordering = ("-created_at",)
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")

    def __str__(self):
        return self.title