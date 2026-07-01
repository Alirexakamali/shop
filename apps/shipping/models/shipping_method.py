from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.base import BaseModel


class ShippingMethod(BaseModel):
    """
    Shipping methods.
    """

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_("Name"),
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=_("Price"),
    )

    estimated_days = models.PositiveSmallIntegerField(
        verbose_name=_("Estimated Days"),
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Is Active"),
    )

    class Meta:
        db_table = "shipping_methods"
        verbose_name = _("Shipping Method")
        verbose_name_plural = _("Shipping Methods")

    def __str__(self):
        return self.name

