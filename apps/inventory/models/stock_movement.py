from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.base import BaseModel


class StockMovement(BaseModel):
    class MovementType(models.TextChoices):
        PURCHASE = "purchase", _("Purchase")
        SALE = "sale", _("Sale")
        RETURN = "return", _("Return")
        ADJUSTMENT = "adjustment", _("Adjustment")

    inventory = models.ForeignKey(
        "inventory.Inventory",
        on_delete=models.CASCADE,
        related_name="movements",
        verbose_name=_("Inventory"),
    )

    movement_type = models.CharField(
        max_length=20,
        choices=MovementType.choices,
        verbose_name=_("Movement Type"),
    )

    quantity = models.IntegerField(
        verbose_name=_("Quantity"),
    )

    description = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Description"),
    )

    class Meta:
        db_table = "stock_movements"
        ordering = ("-created_at",)
        verbose_name = _("Stock Movement")
        verbose_name_plural = _("Stock Movements")

    def __str__(self):
        return f"{self.inventory.variant.sku} ({self.quantity})"