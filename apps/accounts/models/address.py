from django.db import models

from common.models.base import BaseModel


class Address(BaseModel):
    """
    User address.
    """

    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="addresses",
    )

    title = models.CharField(
        max_length=100,
    )

    recipient_name = models.CharField(
        max_length=255,
    )

    recipient_phone = models.CharField(
        max_length=11,
    )

    province = models.CharField(
        max_length=100,
    )

    city = models.CharField(
        max_length=100,
    )

    postal_code = models.CharField(
        max_length=10,
    )

    address = models.TextField()

    building_number = models.CharField(
        max_length=20,
        blank=True,
    )

    unit = models.CharField(
        max_length=20,
        blank=True,
    )

    is_default = models.BooleanField(
        default=False,
    )

    class Meta:
        db_table = "addresses"

    def __str__(self):
        return f"{self.user} - {self.title}"