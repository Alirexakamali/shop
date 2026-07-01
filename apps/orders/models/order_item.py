from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.base import BaseModel



class OrderItem(BaseModel):
    order = models.ForeignKey(
        "order.Order",
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name=_("Order"),
    )

    variant = models.ForeignKey(
        "catalog.ProductVariant",
        on_delete=models.PROTECT,
        related_name="order_items",
        verbose_name=_("Variant"),
    )

    quantity = models.PositiveIntegerField(
        verbose_name=_("Quantity"),
    )

    unit_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=_("Unit Price"),
    )

    total_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=_("Total Price"),
    )

    class Meta:
        db_table = "order_items"
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")

    def __str__(self):
        return f"{self.order} - {self.variant}"