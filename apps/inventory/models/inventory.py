from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.base import BaseModel


class Inventory(BaseModel):
    """
    Inventory information for a product variant.
    """

    variant = models.OneToOneField(
        "catalog.ProductVariant",
        on_delete=models.CASCADE,
        related_name="inventory",
        verbose_name=_("Variant"),
    )

    quantity = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Quantity"),
    )

    reserved_quantity = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Reserved Quantity"),
    )

    low_stock_threshold = models.PositiveIntegerField(
        default=5,
        verbose_name=_("Low Stock Threshold"),
    )

    class Meta:
        db_table = "inventories"
        verbose_name = _("Inventory")
        verbose_name_plural = _("Inventories")

    @property
    def available_quantity(self):
        return self.quantity - self.reserved_quantity

    def __str__(self):
        return self.variant.sku