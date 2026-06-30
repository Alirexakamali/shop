from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.base import BaseModel


class Address(BaseModel):
    """
    User address.
    """

    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="addresses",
        verbose_name=_("User"),
    )

    title = models.CharField(
        max_length=100,
        verbose_name=_("Title"),
    )

    recipient_name = models.CharField(
        max_length=255,
        verbose_name=_("Recipient name"),
    )

    recipient_phone = models.CharField(
        max_length=11,
        verbose_name=_("Recipient phone"),
    )

    province = models.CharField(
        max_length=100,
        verbose_name=_("Province"),
    )

    city = models.CharField(
        max_length=100,
        verbose_name=_("City"),
    )

    postal_code = models.CharField(
        max_length=10,
        verbose_name=_("Postal code"),
    )

    address = models.TextField(
        verbose_name=_("Address"),
    )

    building_number = models.CharField(
        max_length=20,
        blank=True,
        verbose_name=_("Building number"),
    )

    unit = models.CharField(
        max_length=20,
        blank=True,
        verbose_name=_("Unit"),
    )

    is_default = models.BooleanField(
        default=False,
        verbose_name=_("Is default"),
    )

    class Meta:
        db_table = "addresses"
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    def __str__(self):
        return f"{self.user} - {self.title}"