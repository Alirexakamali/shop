from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.base import BaseModel


class Discount(BaseModel):
    class Type(models.TextChoices):
        PERCENT = "percent", _("Percent")
        FIXED = "fixed", _("Fixed Amount")

    code = models.CharField(
        max_length=50,
        unique=True,
        verbose_name=_("Code"),
    )

    discount_type = models.CharField(
        max_length=20,
        choices=Type.choices,
        verbose_name=_("Discount Type"),
    )

    value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Value"),
    )

    max_discount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_("Maximum Discount"),
    )

    minimum_order_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name=_("Minimum Order Amount"),
    )

    usage_limit = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("Usage Limit"),
    )

    used_count = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Used Count"),
    )

    starts_at = models.DateTimeField(
        verbose_name=_("Starts At"),
    )

    expires_at = models.DateTimeField(
        verbose_name=_("Expires At"),
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Is Active"),
    )

    class Meta:
        db_table = "discounts"
        verbose_name = _("Discount")
        verbose_name_plural = _("Discounts")

    def __str__(self):
        return self.code

